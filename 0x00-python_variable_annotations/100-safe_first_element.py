#!/usr/bin/env python3
"""
safe_first_element
This function takes a sequence of any type and returns the first
element if it exists.
If the sequence is empty, it returns None.
"""


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it exists, otherwise returns
    None.

    Args:
        lst (Sequence[Any]): The sequence from which to retrieve the first
        element.

    Returns:
        Optional[Any]: The first element of the sequence if it exists,
        otherwise None.
    """

    if lst:
        return lst[0]
    else:
        return None
