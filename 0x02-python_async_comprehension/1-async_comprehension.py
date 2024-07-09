#!/usr/bin/env python3
'''
    Task: Async Comprehensions
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
         coroutine will collect 10 random numbers:
            Using an async comprehensing over async_generator,
            then return the 10 random numbers
    '''
    return [num async for num in async_generator()]
