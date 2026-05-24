#!/usr/bin/env python3


"""Module that defines a list of floats and integers."""
from typing import List, Union

def sum_mixed_list(mxd_list: List(Union[int, float])) -> float:
    """Return the sum of all float and integer values in a list.

    This function accepts a list of annotated float and integer values and returns
    their total as a single float. It is useful for demonstrating how
    typed input and output can make numeric aggregation clearer.

    Args:
        input_list (List[float]): The list of numbers to sum.

    Returns:
        float: The total of all values in ``input_list``.
    """
    sum = 0
    for i in mxd_list:
        sum += i
    return sum
