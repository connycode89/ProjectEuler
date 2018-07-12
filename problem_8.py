# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 01:23:02 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=8

import numpy as np
import math

def read_data():
    data = np.genfromtxt('p08_num.txt', dtype=str)
    return data

def get_all_n_adjs(n):
    num = str(read_data())
    list1 = []
    for num2 in range(len(num)-n+1):
        list1.append(num[num2:num2+n])
    return list1

def filter_zeros(list1):
    # 0 will never be the largest product so filter out sequences with zeroes
    list2 = filter(lambda x:not '0' in x, list1)
    return list2
     
def do_log_addition(str1):
    logger = map(lambda x:math.log(int(x)), str1)
    log_add = reduce(lambda x,y:x+y, logger)
    return log_add

def get_largest(n2):
    all_nums = get_all_n_adjs(n2)
    all_nums_filt = filter_zeros(all_nums)
    max_log = max(map(lambda x:do_log_addition(x), all_nums_filt))
    largest = int(round(math.exp(max_log)))
    return largest
    
result = get_largest(13)
print result