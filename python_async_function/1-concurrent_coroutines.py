#!/usr/bin/env python3
"""1-concurrent_coroutines

Run `n` sequential awaits of `wait_random` from
`0-basic_async_syntax` and return their results.

This module is part of a small exercise set demonstrating basic
asyncio usage. Use the `wait_n` coroutine to collect `n` results
from `wait_random(max_delay)`.

Example:
    python python_async_function/1-concurrent_coroutines.py 5 3

"""
import asyncio  # <--- BU SƏTRİ MÜTLƏQ ƏLAVƏ ETMƏLİSƏN
import importlib
from typing import List

# Dynamically import the helper module that provides `wait_random`.
basic_async_syntax = importlib.import_module("0-basic_async_syntax")

# Pull the function into this module's namespace for convenience.
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run `n` coroutines that await `wait_random(max_delay)`.

    Args:
        n: Number of times to call and await `wait_random`.
        max_delay: The `max_delay` argument forwarded to `wait_random`.

    Returns:
        A list of floats with the delays returned by each `wait_random` call,
        in the order the calls were awaited.
    """
    result: List[float] = []
    for i in range(n):
        a = await wait_random(max_delay)
        result.append(a)
    return result
