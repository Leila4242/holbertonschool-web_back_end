#!/usr/bin/env python3


"""Module that defines a list of floats and integers."""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple:
    user_data: Tuple[int, Union[int, float]] = (k, v)
    return user_data

