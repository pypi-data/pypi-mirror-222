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

from .base import StorageLevel, get_storage_backend
from .cuda import CudaStorage
from .filesystem import FileSystemStorage
from .shared_memory import SharedMemoryStorage

try:
    # require vineyard, pyarrow
    from .vineyard import VineyardStorage
except ImportError:
    pass
try:
    # require pyarrow
    from .plasma import PlasmaStorage
except ImportError:
    pass
