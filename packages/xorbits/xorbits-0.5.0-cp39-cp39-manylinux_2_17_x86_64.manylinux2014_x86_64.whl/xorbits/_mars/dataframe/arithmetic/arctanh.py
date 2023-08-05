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

from ... import opcodes as OperandDef
from ...utils import classproperty
from .core import DataFrameUnaryUfunc


class DataFrameArctanh(DataFrameUnaryUfunc):
    _op_type_ = OperandDef.ARCTANH
    _func_name = "arctanh"

    @classproperty
    def tensor_op_type(self):
        from ...tensor.arithmetic import TensorArctanh

        return TensorArctanh
