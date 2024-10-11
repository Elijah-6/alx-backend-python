#!/usr/bin/env python3
"""
This module provides a function to safely retrieve a value from a dictionary.
Functions:
    safely_get_value(dct: Mapping[Any, T], key: Any, default: T = None) -> T:
        Safely retrieves a value from a dictionary. If the key is not present,
        returns the default value.
Parameters:
    dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
    key (Any): The key to look up in the dictionary.
    default (T, optional): The default value to return if the key is not found.
        Defaults to None.
Returns:
    T: The value associated with the key if it exists, otherwise the default
    value.
"""

from typing import Any, TypeVar, Mapping, Union
from types import NoneType

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[T, NoneType]) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
