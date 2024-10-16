#!/usr/bin/env python3
"""
This module contains a function `make_multiplier` that creates a multiplier
function.
Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Returns a function that multiplies its input by the given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier(multiplier: float) -> Callable[[float], float]

    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of that float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
