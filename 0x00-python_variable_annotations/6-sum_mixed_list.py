#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.
Function:
    sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        Sums a list containing both integers and floats and returns the result
        as a float.
Args:
    mxd_lst (List[Union[int, float]]): A list containing integers and floats.
Returns:
    float: The sum of the elements in the list.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
