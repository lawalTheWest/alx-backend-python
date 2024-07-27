#!/usr/bin/env python3
'''
    unit test for utils.access_nested_map
'''
import unittest
from unittest.mock import patch
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    '''
        Test nested map class
    '''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
        ])
    def test_access_nested_map(self, map, path, expected_output):
        '''
            to return correct output
        '''
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameteerized.expand([
        ({}, ('a',), 'a'),
        ({'a': 1}, ('a', 'b'), 'b')
        ])
    def test_access_nested_map_exception(self, map, path,     wrong_output):
        '''
        '''
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)

        self.assertEqual(str(e.exception)[1:-1], wrong_output)
