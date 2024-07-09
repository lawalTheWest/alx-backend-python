#!/usr/bin/env python3
'''
    Task: Async Generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
         a coroutine called async_generator that takes no arguments
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
