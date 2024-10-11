#!/usr/bin/env python3
"""
This module contains a function `concat` that concatenates two strings.
Functions:
    concat(str1: str, str2: str) -> str:
        Returns the concatenated result of str1 and str2.
        Example:
            concat("hello", "world") -> "helloworld"
            concat("123", "456") -> "123456"
            concat("abc", "def") -> "abcdef"
            concat("abc", "") -> "abc"
            concat("", "def") -> "def"
            concat("", "") -> ""
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated result of str1 and str2.
    """

    return str1 + str2
