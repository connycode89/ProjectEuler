# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 01:23:02 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=13

import pandas as pd
import numpy as np

def read_data_sum_dict(filename):
    arr1 = np.genfromtxt(filename, dtype=str)
    df = pd.DataFrame(map(lambda x:[y for y in x], arr1), columns=range(49,-1,-1)).astype(int)
    summed = dict(df.sum(axis=0))
    return summed

def manipulate_dict(filename2):
    dict_sum = read_data_sum_dict(filename2)
    for num in sorted(dict_sum.keys()):
        if num!=0:
            dict_sum[num] += dict_sum[num-1]/10
    for num2 in sorted(dict_sum.keys()):
        if num2!=49:
            dict_sum[num2] = dict_sum[num2]%10
    return dict_sum

def get_total_sum(filename3):
    sum_dict = manipulate_dict(filename3)
    summed2 = ''
    for num3 in sorted(sum_dict.keys(), reverse=True):
        summed2 += str(sum_dict[num3])
    return summed2

sum1 = get_total_sum('p013_nums.txt')
result = sum1[:10]
print result