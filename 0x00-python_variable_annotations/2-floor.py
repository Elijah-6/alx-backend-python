#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a floating-point
number.
Functions:
    floor(n: float) -> int: Returns the floor of the given floating-point
    number.
"""


import math


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to the given float.

    Args:
        n (float): The float number to be floored.

    Returns:
        int: The largest integer less than or equal to the given float.
    """

    return math.floor(n)
