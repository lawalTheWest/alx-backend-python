#!/usr/bin/env python3
'''
    Module 9-element_length
    Returns list
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns values with appropriate types'''
    return [(i, len(i)) for i in lst]
