#!/usr/bin/env python3
'''
    Module 8-make_multiplier
    Returns a function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''This returns a function'''
    def mltply(n: float) -> float:
        '''this returns the product'''
        return multiplier * n
    return mltply
