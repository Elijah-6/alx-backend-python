#!/usr/bin/env python3
"""
This module contains a function to compute the length of elements in a list of
strings.
Functions:
    element_length(lst: List[str]) -> List[Tuple[str, int]]:
        Computes the length of each string in the input list and returns a list
        of tuples,
        where each tuple contains a string and its corresponding length.
Args:
    lst (List[str]): A list of strings.
Returns:
    List[Tuple[str, int]]: A list of tuples, each containing a string from the
    input list and its length.
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of sequences and returns a list of tuples, where each tuple
    contains a sequence from the input list and its corresponding length.

    Args:
        lst (Iterable[Sequence]): A list of sequences (e.g., strings, lists,
        tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence from the input list and its length.
    """

    return [(i, len(i)) for i in lst]
