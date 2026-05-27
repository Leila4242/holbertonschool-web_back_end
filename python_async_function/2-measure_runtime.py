#!/usr/bin/env python3


import asyncio  # <--- BU SƏTRİ MÜTLƏQ ƏLAVƏ ETMƏLİSƏN
import importlib
import time
from typing import List

# Dynamically import the helper module that provides `wait_random`.
basic_async_syntax = importlib.import_module("1-concurrent_coroutines")

# Pull the function into this module's namespace for convenience.
wait_n = basic_async_syntax.wait_n


async def measure_time(n: int, max_delay: int) -> float:
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    return (end_time-start_time)/n
