#!/usr/bin/env python3
'''
    Module 6-sum_mixed_list
    Returns sum as float
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
        Takes a list of integers and floats
        Returns sum as float
    '''
    return sum(mxd_lst)
