#!/usr/bin/env python3
"""
This module provides a function to zoom into an array by repeating its
elements.
Functions:
    zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
        Zooms into the given tuple by repeating each element 'factor' times.
Variables:
    array (Tuple[int, ...]): A tuple of integers to be zoomed.
    zoom_2x (List[int]): The result of zooming 'array' by a factor of 2.
    zoom_3x (List[int]): The result of zooming 'array' by a factor of 3.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
