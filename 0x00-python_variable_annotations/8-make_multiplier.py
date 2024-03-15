#!/usr/bin/env python3
"""a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by a multiplier"""

    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
