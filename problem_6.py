# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 00:25:17 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=6

import numpy as np

def gen_first_n_nums(n):
    nums = np.arange(1,n+1)
    return nums

def sum_n_nums_squared(n2):
    list1 = gen_first_n_nums(n2)
    sum1 = (list1[0]+list1[-1])*len(list1)/2
    return sum1**2

def sum_of_n_squares(n3):
    n3 = float(n3)
    sum2 = (n3*(n3+1)*(2*n3+1))/6
    return int(sum2)

def diff(n4):
    difference = sum_n_nums_squared(n4)-sum_of_n_squares(n4)
    return difference

print diff(100)