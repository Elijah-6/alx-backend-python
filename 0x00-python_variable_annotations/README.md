# Python Variable Annotations

This repository contains various Python scripts demonstrating the use of type annotations. Each script focuses on a specific functionality, showcasing how type annotations can be used to improve code readability and maintainability.

## Table of Contents

1. [concat.py](#1-concatpy)
2. [add.py](#0-addpy)
3. [floor.py](#2-floorpy)
4. [to_str.py](#3-to_strpy)
5. [sum_list.py](#5-sum_listpy)
6. [sum_mixed_list.py](#6-sum_mixed_listpy)
7. [to_kv.py](#7-to_kvpy)
8. [make_multiplier.py](#8-make_multiplierpy)
9. [element_length.py](#9-element_lengthpy)
10. [safe_first_element.py](#100-safe_first_elementpy)
11. [safely_get_value.py](#101-safely_get_valuepy)
12. [type_checking.py](#102-type_checkingpy)

## 1. concat.py

This module contains a function `concat` that concatenates two strings.

### Function

- `concat(str1: str, str2: str) -> str`: Returns the concatenated result of `str1` and `str2`.

## 0. add.py

This module contains a function that adds two floating-point numbers.

### Function

- `add(a: float, b: float) -> float`: Returns the sum of the two numbers.

## 2. floor.py

This module provides a function to compute the floor of a floating-point number.

### Function

- `floor(n: float) -> int`: Returns the floor of the given floating-point number.

## 3. to_str.py

This module contains a function that converts a float to a string.

### Function

- `to_str(n: float) -> str`: Converts a float to its string representation.

## 5. sum_list.py

This module provides a function to sum a list of floating point numbers.

### Function

- `sum_list(input_list: List[float]) -> float`: Returns the sum of all the numbers in the input list.

## 6. sum_mixed_list.py

This module provides a function to sum a list of integers and floats.

### Function

- `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`: Sums a list containing both integers and floats and returns the result as a float.

## 7. to_kv.py

This module contains a function `to_kv` that takes a string and a number, and returns a tuple with the string and the square of the number as a float.

### Function

- `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`: Takes a string and a number, and returns a tuple with the string and the square of the number as a float.

## 8. make_multiplier.py

This module contains a function `make_multiplier` that creates a multiplier function.

### Function

- `make_multiplier(multiplier: float) -> Callable[[float], float]`: Returns a function that multiplies its input by the given multiplier.

## 9. element_length.py

This module contains a function to compute the length of elements in a list of strings.

### Function

- `element_length(lst: List[str]) -> List[Tuple[str, int]]`: Computes the length of each string in the input list and returns a list of tuples, where each tuple contains a string and its corresponding length.

## 100. safe_first_element.py

This module contains a function `safe_first_element` that takes a sequence of any type and returns the first element if it exists. If the sequence is empty, it returns `None`.

### Function

- `safe_first_element(lst: Sequence[Any]) -> Optional[Any]`: Returns the first element of the sequence if it exists, otherwise `None`.

## 101. safely_get_value.py

This module provides a function to safely retrieve a value from a dictionary.

### Function

- `safely_get_value(dct: Mapping[Any, T], key: Any, default: T = None) -> T`: Safely retrieves a value from a dictionary. If the key is not present, returns the default value.

## 102. type_checking.py

This module provides a function to zoom into an array by repeating its elements.

### Function

- `zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]`: Zooms into the given tuple by repeating each element 'factor' times.

### Variables

- `array (Tuple[int, ...])`: A tuple of integers to be zoomed.
- `zoom_2x (List[int])`: The result of zooming `array` by a factor of 2.
- `zoom_3x (List[int])`: The result of zooming `array` by a factor of 3.
