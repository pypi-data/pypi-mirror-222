# Copyright (c) 2016-2022 Association of Universities for Research in Astronomy, Inc. (AURA)
# For license information see LICENSE or https://opensource.org/licenses/BSD-3-Clause

# Basic type aliases for usefulness.
from datetime import timedelta
from typing import Final, List, TypeVar, Union

import numpy.typing as npt
from astropy.time import Time  # type: ignore

T = TypeVar('T')

ScalarOrNDArray = Union[T, npt.NDArray[T]]
TimeScalarOrNDArray = Union[Time, npt.NDArray[float]]
ListOrNDArray = Union[List[T], npt.NDArray[T]]

ZeroTime: Final[timedelta] = timedelta()
# Convenient type alias for Interval
Interval = npt.NDArray[int]
