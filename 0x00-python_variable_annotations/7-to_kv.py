#!/usr/bin/env python3
"""
This module contains a function to_kv that takes a string and a number,
and returns a tuple with the string and the square of the number as a float.
Functions:
    to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        Takes a string and a number, and returns a tuple with the string and
        the square of the number as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and a value to a tuple where the value is squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the key and
        the squared value as a float.
    """
    return (k, float(v ** 2))
