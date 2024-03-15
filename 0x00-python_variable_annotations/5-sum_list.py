#!/usr/bin/env python3
"""a type-annotated function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum list of float"""
    n: float = 0.0
    for i in input_list:
        n += i
    return n
