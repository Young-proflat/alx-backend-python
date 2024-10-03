#!/usr/bin/env python3
""" define caroutine """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
