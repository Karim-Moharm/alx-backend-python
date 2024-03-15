#!/usr/bin/env python3
"""a type-annotated function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of list in float"""
    n: float = 0.0
    for i in mxd_lst:
        n += i
    return n
