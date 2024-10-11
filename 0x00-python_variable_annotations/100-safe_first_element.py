#!/usr/bin/env python3
"""
safe_first_element
This function takes a sequence of any type and returns the first
element if it exists.
If the sequence is empty, it returns None.
Parameters:
    lst (Sequence[Any]): A sequence of elements of any type.
Returns:
    Optional[Any]: The first element of the sequence if it exists,
    otherwise None.
"""


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
