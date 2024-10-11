#!/usr/bin/env python3
"""
This module provides a function to sum a list of floating point numbers.
Functions:
    sum_list(input_list: List[float]) -> float:
        Returns the sum of all the numbers in the input list.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
