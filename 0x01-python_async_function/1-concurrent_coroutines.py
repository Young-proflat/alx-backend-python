#!/usr/bin/env python3

import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

asyncio def wait_n(n:int, max_delay:int) -> List[float]:
    
    wait_times = await asyncio.gather(*tuple(map(lambda_: wait_random(max_delay), range(n)))
            )
    return sorted(wait_times)
