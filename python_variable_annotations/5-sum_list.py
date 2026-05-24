#!/usr/bin/env python3

"""Module that defines a list of floats."""
from typing import List


# Defining and annotating the function
def sum_list(input_list: List[float]) -> float:
    sum = 0
    for i in input_list:
        sum += i
    return sum
