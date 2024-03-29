#!/usr/bin/env python3
"""duck type annitation
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return first element ot None if list are not exist"""
    if lst:
        return lst[0]
    else:
        return None
