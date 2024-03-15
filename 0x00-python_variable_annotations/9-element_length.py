#!/usr/bin/env pyhon3
"""annotation of a function
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """length of elements in list"""
    return [(i, len(i)) for i in lst]
