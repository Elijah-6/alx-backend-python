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
    return (k, float(v ** 2))
