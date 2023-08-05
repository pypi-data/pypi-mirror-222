# Copyright 2022-2023 XProbe Inc.
# derived from copyright 1999-2021 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

import xoscar as mo
from xoscar.backends.allocate_strategy import IdleLabel, NoIdleSlot

from ...lib.aio import AioFileObject
from ...resource import cuda_card_stats
from ...storage import StorageLevel, get_storage_backend
from ...storage.base import ObjectInfo, StorageBackend
from ...storage.core import StorageFileObject
from ...utils import dataslots
from .errors import DataNotExist, StorageFull

logger = logging.getLogger(__name__)


def build_data_info(storage_info: ObjectInfo, level, size, band_name=None):
    # todo handle multiple
    if band_name is None:
        band_name = (
            "numa-0" if storage_info.device is None else f"gpu-{storage_info.device}"
        )
    if storage_info.size is None:
        store_size = size
    else:
        store_size = storage_info.size
    return DataInfo(storage_info.object_id, level, size, store_size, band_name)


class WrappedStorageFileObject(AioFileObject):
    """
    Wrap to hold ref after write close
    """

    def __init__(
        self,
        file: StorageFileObject,
        level: StorageLevel,
        size: int,
        session_id: str,
        data_key: Union[str, Tuple],
        data_manager: mo.ActorRefType["DataManagerActor"],
        storage_handler: StorageBackend,
        band_name: str = "numa-0",
    ):
        self._object_id = file.object_id
        super().__init__(file)
        self._size = size
        self._level = level
        self._session_id = session_id
        self._data_key = data_key
        self._data_manager = data_manager
        self._storage_handler = storage_handler
        self._band_name = band_name
        # infos for multiple data
        self._sub_key_infos = dict()

    def __getattr__(self, item):
        if hasattr(self._file, item):
            return getattr(self._file, item)

    def set_file_header(self, header: Any):
        if hasattr(self._file, "header"):
            self._file.header = header

    def set_buffers_by_sizes(self, sizes: List):
        if hasattr(self._file, "set_buffers_by_sizes"):
            self._file.set_buffers_by_sizes(sizes)

    def commit_once(self, sub_key: Tuple, offset: int, size: int):
        self._sub_key_infos[sub_key] = (offset, size)

    async def clean_up(self):
        self._file.close()

    async def close(self):
        self._file.close()
        if self._object_id is None:
            # for some backends like vineyard,
            # object id is generated after write close
            self._object_id = self._file.object_id
        if "w" in self._file.mode:
            object_info = await self._storage_handler.object_info(self._object_id)
            object_info.size = self._size
            data_info = build_data_info(
                object_info, self._level, self._size, band_name=self._band_name
            )
            await self._data_manager.put_data_info(
                self._session_id,
                self._data_key,
                data_info,
                object_info,
                self._sub_key_infos,
            )


class StorageQuotaActor(mo.Actor):
    def __init__(
        self,
        data_manager: mo.ActorRefType["DataManagerActor"],
        level: StorageLevel,
        total_size: Optional[Union[int, float]],
    ):
        self._data_manager = data_manager
        self._total_size = total_size if total_size is None else total_size * 0.95
        self._used_size = 0
        self._level = level

    @classmethod
    def gen_uid(cls, band_name: str, level: StorageLevel):
        return f"storage_quota_{band_name}_{level}"

    def update_quota(self, size: int):
        self._used_size += size
        logger.debug(
            "Update %s bytes of %s, used size now is %s",
            size,
            self._level,
            self._used_size,
        )

    def request_quota(self, size: int) -> bool:
        if self._total_size is not None and size > self._total_size:  # pragma: no cover
            raise StorageFull(
                f"Request size {size} is larger than total size {self._total_size}"
            )
        if self._total_size is not None and self._used_size + size > self._total_size:
            logger.debug(
                "Request %s bytes of %s, used size now is %s,"
                "space is not enough for the request",
                size,
                self._level,
                self._used_size,
            )
            return False
        else:
            self._used_size += size
            logger.debug(
                "Request %s bytes of %s, used size now is %s, total size is %s",
                size,
                self._level,
                self._used_size,
                self._total_size,
            )
            return True

    def release_quota(self, size: int):
        self._used_size -= size
        logger.debug(
            "Release %s bytes of %s, used size now is %s, total size is %s",
            size,
            self._level,
            self._used_size,
            self._total_size,
        )

    def get_quota(self) -> Tuple[float, float]:
        return self._total_size, self._used_size


@dataslots
@dataclass
class DataInfo:
    object_id: object
    level: StorageLevel
    memory_size: int
    store_size: int
    band: str = None
    offset: int = None


@dataslots
@dataclass
class InternalDataInfo:
    data_info: DataInfo
    object_info: ObjectInfo


@dataslots
@dataclass
class SubInfo:
    store_key: str
    offset: int
    size: int


class DataManagerActor(mo.Actor):
    _data_key_to_infos: Dict[Tuple, List[InternalDataInfo]]
    _data_info_list: Dict[Tuple, Dict]
    _spill_strategy: Dict[Tuple, Any]
    _sub_key_to_sub_info: Dict[Tuple, SubInfo]
    _store_key_to_sub_infos: Dict[Tuple, Dict[Tuple, SubInfo]]

    def __init__(self, bands: List):
        from .spill import FIFOStrategy

        # mapping key is (session_id, data_key)
        # mapping value is list of InternalDataInfo
        self._bands = bands
        self._data_key_to_infos = defaultdict(list)
        self._data_info_list = dict()
        self._spill_strategy = dict()
        # data key may be a tuple in shuffle cases,
        # we record the mapping from main key to sub keys,
        # it's used when decref mapper data using main key
        self._main_key_to_sub_keys = defaultdict(set)
        # we may store multiple small data into one file,
        # it records offset and size.
        self._sub_key_to_sub_info = dict()
        self._store_key_to_sub_infos = dict()
        for level in StorageLevel.__members__.values():
            for band_name in bands:
                self._data_info_list[level, band_name] = dict()
                self._spill_strategy[level, band_name] = FIFOStrategy(level)

    @mo.extensible
    def get_data_infos(
        self,
        session_id: str,
        data_key: Union[str, Tuple],
        band_name: str,
        error: str = "raise",
    ) -> Optional[Union[List[DataInfo], Dict]]:
        if (session_id, data_key) in self._data_key_to_infos:
            available_infos = []
            for info in self._data_key_to_infos[session_id, data_key]:
                info_band = info.data_info.band
                if info_band.startswith("gpu-"):  # pragma: no cover
                    # not available for different GPU bands
                    if info_band == band_name:
                        available_infos.append(info.data_info)
                else:
                    available_infos.append(info.data_info)
            return available_infos
        else:
            if error == "raise":
                raise DataNotExist(f"Data key {session_id, data_key} not exists.")
            else:
                return

    @mo.extensible
    def get_data_info(
        self,
        session_id: str,
        data_key: Union[str, Tuple],
        band_name: str = None,
        error: str = "raise",
    ) -> Union[DataInfo, None]:
        sub_info = None
        if (session_id, data_key) in self._sub_key_to_sub_info:
            sub_info = self._sub_key_to_sub_info[(session_id, data_key)]
            data_key = sub_info.store_key

        # if the data is stored in multiply levels,
        # return the lowest level info
        infos = self.get_data_infos(session_id, data_key, band_name, error)
        if not infos:
            return
        info = sorted(infos, key=lambda x: x.level)[0]
        if sub_info is not None:
            return DataInfo(
                info.object_id,
                info.level,
                sub_info.size,
                sub_info.size,
                info.band,
                sub_info.offset,
            )
        else:
            return info

    @mo.extensible
    def put_data_info(
        self,
        session_id: str,
        data_key: Union[str, Tuple],
        data_info: DataInfo,
        object_info: ObjectInfo = None,
        sub_key_infos: Dict = None,
    ):
        info = InternalDataInfo(data_info, object_info)
        self._data_key_to_infos[(session_id, data_key)].append(info)
        self._data_info_list[data_info.level, data_info.band][
            (session_id, data_key)
        ] = object_info
        self._spill_strategy[data_info.level, data_info.band].record_put_info(
            (session_id, data_key), data_info.store_size
        )
        if sub_key_infos:
            for key, (offset, size) in sub_key_infos.items():
                self._sub_key_to_sub_info[(session_id, key)] = SubInfo(
                    data_key, offset, size
                )
            self._store_key_to_sub_infos[(session_id, data_key)] = sub_key_infos
        if isinstance(data_key, tuple):
            self._main_key_to_sub_keys[(session_id, data_key[0])].add(data_key)

    @mo.extensible
    def delete_data_info(
        self,
        session_id: str,
        data_key: Union[str, Tuple],
        level: StorageLevel,
        band_name: str,
    ):
        if (session_id, data_key) in self._data_key_to_infos:
            self._data_info_list[level, band_name].pop((session_id, data_key))
            self._spill_strategy[level, band_name].record_delete_info(
                (session_id, data_key)
            )
            infos = self._data_key_to_infos[(session_id, data_key)]
            rest = [info for info in infos if info.data_info.level != level]
            if len(rest) == 0:
                del self._data_key_to_infos[(session_id, data_key)]
            else:  # pragma: no cover
                self._data_key_to_infos[(session_id, data_key)] = rest

    @mo.extensible
    def get_store_key(self, session_id: str, data_key: Union[str, Tuple, List]):
        if (session_id, data_key) in self._sub_key_to_sub_info:
            return self._sub_key_to_sub_info[(session_id, data_key)].store_key
        elif (session_id, data_key) in self._main_key_to_sub_keys:
            # only into when delete mapper main key
            return list(self._main_key_to_sub_keys[(session_id, data_key)])
        else:
            return data_key

    @mo.extensible
    def get_sub_infos(self, session_id: str, store_key: str):
        if (session_id, store_key) in self._store_key_to_sub_infos:
            return self._store_key_to_sub_infos[(session_id, store_key)]
        else:
            return None

    def list(self, level: StorageLevel, band_name: str):
        return list(self._data_info_list[level, band_name].keys())

    @mo.extensible
    def pin(self, session_id, data_key, band_name, error="raise"):
        info = self.get_data_info(session_id, data_key, band_name, error=error)
        if info is not None:
            self._spill_strategy[info.level, info.band].pin_data((session_id, data_key))

    @mo.extensible
    def unpin(
        self,
        session_id: str,
        data_keys: List[str],
        band_name: str,
        error: str = "raise",
    ):
        if error not in ("raise", "ignore"):  # pragma: no cover
            raise ValueError("error must be raise or ignore")
        levels = set()
        for data_key in data_keys:
            info = self.get_data_info(session_id, data_key, band_name, error)
            if info:
                level = info.level
                self._spill_strategy[level, info.band].unpin_data(
                    (session_id, data_key)
                )
                levels.add(level)
        return list(levels)

    def get_spillable_size(self, level: StorageLevel, band_name: str):
        return self._spill_strategy[level, band_name].get_spillable_size()

    async def get_spill_keys(self, level: StorageLevel, band_name: str, size: int):
        return self._spill_strategy[level, band_name].get_spill_keys(size)


class StorageManagerActor(mo.StatelessActor):
    """
    Storage manager actor, created only on main process, mainly to setup storage backends
    and create all the necessary actors for storage service.
    """

    _data_manager: mo.ActorRefType[DataManagerActor]

    def __init__(
        self, storage_configs: Dict, transfer_block_size: int = None, **kwargs
    ):
        from .handler import StorageHandlerActor

        self._handler_cls = kwargs.pop("storage_handler_cls", StorageHandlerActor)
        self._storage_configs = storage_configs
        self._all_bands = None
        self._cluster_api = None
        self._upload_task = None

        # params to init and teardown
        self._init_params = defaultdict(dict)
        self._teardown_params = defaultdict(dict)
        self._supervisor_address = None

        # transfer config
        self._transfer_block_size = transfer_block_size
        self._quotas = None
        self._spill_managers = None

    async def __post_create__(self):
        from ..cluster.api import ClusterAPI

        try:
            self._cluster_api = cluster_api = await ClusterAPI.create(self.address)
            band_to_resource = await cluster_api.get_bands()
            self._all_bands = [band[1] for band in band_to_resource]
        except mo.ActorNotExist:
            # in some test cases, cluster service is not available
            self._all_bands = ["numa-0"]
        await self._handle_post_create()

    async def _handle_post_create(self):
        from .handler import StorageHandlerActor

        # stores the mapping from data key to storage info
        self._data_manager = await mo.create_actor(
            DataManagerActor,
            self._all_bands,
            uid=DataManagerActor.default_uid(),
            address=self.address,
        )

        # setup storage backend
        await self._setup_storage_backends()

        # create in main process
        default_band_name = "numa-0"
        await mo.create_actor(
            self._handler_cls,
            self._init_params[default_band_name],
            self._data_manager,
            self._spill_managers[default_band_name],
            self._quotas[default_band_name],
            default_band_name,
            uid=StorageHandlerActor.gen_uid(default_band_name),
            address=self.address,
        )

        # create handler actors for every process
        await self._create_storage_handler_actors()
        # create actor for transfer
        await self._create_transfer_actors()
        await self.upload_disk_info()
        # create task for uploading storage usages
        self._upload_task = asyncio.create_task(self.upload_storage_info())

    async def __pre_destroy__(self):
        if self._upload_task:
            self._upload_task.cancel()
        for _, params in self._teardown_params.items():
            for backend, teardown_params in params.items():
                backend_cls = get_storage_backend(backend)
                await backend_cls.teardown(**teardown_params)

    async def _setup_storage_backends(self):
        from .spill import SpillManagerActor

        self._quotas = quotas = defaultdict(dict)
        self._spill_managers = spill_managers = defaultdict(dict)
        for backend, setup_params in self._storage_configs.items():
            if backend == "cuda":  # pragma: no cover
                cuda_infos = await asyncio.to_thread(cuda_card_stats)
                storage_bands = [s for s in self._all_bands if s.startswith("gpu-")]
                clients = []
                for gpu_band in storage_bands:
                    index = int(gpu_band[4:])
                    size = cuda_infos[index].fb_mem_info.available
                    params = dict(size=size, **setup_params)
                    clients.append(await self._setup_storage(gpu_band, backend, params))
            else:
                storage_bands = ["numa-0"]
                clients = [
                    await self._setup_storage(band_name, backend, setup_params)
                    for band_name in storage_bands
                ]

            for level in StorageLevel.__members__.values():
                for client, storage_band in zip(clients, storage_bands):
                    if client.level & level:
                        logger.debug(
                            "Create quota manager for %s, total size is %s",
                            level,
                            client.size,
                        )
                        quotas[storage_band][level] = await mo.create_actor(
                            StorageQuotaActor,
                            self._data_manager,
                            level,
                            client.size,
                            uid=StorageQuotaActor.gen_uid(storage_band, level),
                            address=self.address,
                        )
                        spill_managers[storage_band][level] = await mo.create_actor(
                            SpillManagerActor,
                            level,
                            uid=SpillManagerActor.gen_uid(storage_band, level),
                            address=self.address,
                        )

    async def _create_storage_handler_actors(self):
        from .handler import StorageHandlerActor
        from .transfer import ReceiverManagerActor, SenderManagerActor

        for band_name in self._init_params:
            strategy = IdleLabel(band_name, "StorageHandler")
            sender_strategy = IdleLabel(band_name, "sender")
            receiver_strategy = IdleLabel(band_name, "receiver")
            init_params = self._get_band_init_params(band_name)
            band_spill_managers = self._get_band_spill_managers(band_name)
            band_quotas = self._get_band_quota_refs(band_name)
            while True:
                try:
                    handler_ref = await mo.create_actor(
                        self._handler_cls,
                        init_params,
                        self._data_manager,
                        band_spill_managers,
                        band_quotas,
                        band_name,
                        uid=StorageHandlerActor.gen_uid(band_name),
                        address=self.address,
                        allocate_strategy=strategy,
                    )
                    # create transfer actor for GPU bands
                    if band_name.startswith("gpu-"):  # pragma: no cover
                        await mo.create_actor(
                            SenderManagerActor,
                            band_name,
                            data_manager_ref=self._data_manager,
                            storage_handler_ref=handler_ref,
                            uid=SenderManagerActor.gen_uid(band_name),
                            address=self.address,
                            allocate_strategy=sender_strategy,
                        )
                        await mo.create_actor(
                            ReceiverManagerActor,
                            band_quotas,
                            handler_ref,
                            address=self.address,
                            uid=ReceiverManagerActor.gen_uid(band_name),
                            allocate_strategy=receiver_strategy,
                        )
                except NoIdleSlot:
                    break

    async def _create_transfer_actors(self):
        from .handler import StorageHandlerActor
        from .transfer import ReceiverManagerActor, SenderManagerActor

        default_band_name = "numa-0"
        sender_strategy = IdleLabel("io", "sender")
        receiver_strategy = IdleLabel("io", "receiver")
        handler_strategy = IdleLabel("io", "handler")
        while True:
            try:
                handler_ref = await mo.create_actor(
                    self._handler_cls,
                    self._init_params[default_band_name],
                    self._data_manager,
                    self._spill_managers[default_band_name],
                    self._quotas[default_band_name],
                    default_band_name,
                    uid=StorageHandlerActor.gen_uid(default_band_name),
                    address=self.address,
                    allocate_strategy=handler_strategy,
                )
                await mo.create_actor(
                    SenderManagerActor,
                    data_manager_ref=self._data_manager,
                    storage_handler_ref=handler_ref,
                    uid=SenderManagerActor.gen_uid(default_band_name),
                    address=self.address,
                    allocate_strategy=sender_strategy,
                )

                await mo.create_actor(
                    ReceiverManagerActor,
                    self._quotas[default_band_name],
                    handler_ref,
                    address=self.address,
                    uid=ReceiverManagerActor.gen_uid(default_band_name),
                    allocate_strategy=receiver_strategy,
                )
            except NoIdleSlot:
                break

    def _get_band_init_params(self, band_name):
        init_params = self._init_params["numa-0"].copy()
        init_params.update(self._init_params[band_name])
        return init_params

    def _get_band_quota_refs(self, band_name):
        band_quotas = self._quotas[band_name].copy()
        band_quotas.update(self._quotas["numa-0"])
        return band_quotas

    def _get_band_spill_managers(self, band_name):
        band_spill_managers = self._spill_managers[band_name].copy()
        band_spill_managers.update(self._spill_managers["numa-0"])
        return band_spill_managers

    async def _setup_storage(
        self, band_name: str, storage_backend: str, storage_config: Dict
    ):
        backend = get_storage_backend(storage_backend)
        storage_config = storage_config or dict()
        init_params, teardown_params = await backend.setup(**storage_config)
        client = backend(**init_params)
        self._init_params[band_name][storage_backend] = init_params
        self._teardown_params[band_name][storage_backend] = teardown_params
        return client

    def get_client_params(self):
        return self._init_params

    async def upload_storage_info(self):
        from ..cluster import StorageInfo

        if self._cluster_api is not None:
            while True:
                try:
                    upload_tasks = []
                    for band, level_to_quota in self._quotas.items():
                        for level, quota_ref in level_to_quota.items():
                            total, used = await quota_ref.get_quota()
                            used = int(used)
                            if total is not None:
                                total = int(total)
                            storage_info = StorageInfo(
                                storage_level=level, total_size=total, used_size=used
                            )
                            upload_tasks.append(
                                self._cluster_api.set_band_storage_info.delay(
                                    band, storage_info
                                )
                            )
                    await self._cluster_api.set_band_storage_info.batch(*upload_tasks)
                except asyncio.CancelledError:  # pragma: no cover
                    break
                except RuntimeError as ex:  # pragma: no cover
                    if "cannot schedule new futures" in str(ex):
                        # when atexit is triggered, the default pool might be shutdown
                        # and to_thread will fail
                        break
                await asyncio.sleep(0.5)

    async def upload_disk_info(self):
        from ..cluster import DiskInfo

        disk_infos = []
        if (
            self._cluster_api is not None
            and "filesystem" in self._init_params["numa-0"]
        ):
            if self._init_params["numa-0"]["filesystem"]["level"] == StorageLevel.DISK:
                params = self._init_params["numa-0"]["filesystem"]
                size = params["size"]
                for path in params["root_dirs"]:
                    disk_infos.append(DiskInfo(path=path, limit_size=size))
                await self._cluster_api.set_node_disk_info(disk_infos)
