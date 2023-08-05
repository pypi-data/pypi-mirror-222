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
from ...config import options
from ...core import OutputType
from .core import DataFrameReductionMixin, DataFrameReductionOperand


class DataFrameMax(DataFrameReductionOperand, DataFrameReductionMixin):
    _op_type_ = OperandDef.MAX
    _func_name = "max"

    @property
    def is_atomic(self):
        return True


def max_series(df, axis=None, skipna=True, level=None, combine_size=None, method=None):
    use_inf_as_na = options.dataframe.mode.use_inf_as_na
    op = DataFrameMax(
        axis=axis,
        skipna=skipna,
        level=level,
        combine_size=combine_size,
        output_types=[OutputType.scalar],
        use_inf_as_na=use_inf_as_na,
        method=method,
    )
    return op(df)


def max_dataframe(
    df,
    axis=None,
    skipna=True,
    level=None,
    numeric_only=None,
    combine_size=None,
    method=None,
):
    use_inf_as_na = options.dataframe.mode.use_inf_as_na
    op = DataFrameMax(
        axis=axis,
        skipna=skipna,
        level=level,
        numeric_only=numeric_only,
        combine_size=combine_size,
        output_types=[OutputType.series],
        use_inf_as_na=use_inf_as_na,
        method=method,
    )
    return op(df)


def max_index(df, axis=None, skipna=True):
    use_inf_as_na = options.dataframe.mode.use_inf_as_na
    op = DataFrameMax(
        axis=axis,
        skipna=skipna,
        output_types=[OutputType.scalar],
        use_inf_as_na=use_inf_as_na,
    )
    return op(df)
