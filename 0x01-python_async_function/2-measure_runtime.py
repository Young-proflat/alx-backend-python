#!/usr/bin/env python3
""" define function to measure runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total exec time for wait_n(n, max_delay)
        return total_time / n
    """
    start = time.perf_counter()
    delays = asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end / n
