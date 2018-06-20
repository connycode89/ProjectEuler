# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:59:34 2018

@author: jdonovc
"""

# Python 2.7
# https://projecteuler.net/problem=22

import string

def read_data():
    with open('p022_names.txt') as f:
        for line in f:
            line = line.strip()
    line = line.replace('"', '')
    name_list = line.split(',')
    return name_list

def get_name_value(name):
    alphabet = string.ascii_uppercase
    dict1 = dict(zip(alphabet, range(1, len(alphabet)+1)))
    value = sum(map(lambda x:dict1[x], name))
    return value
  
def total_name_scores():          
    list_names = sorted(read_data())
    all_name_vals = map(lambda x:get_name_value(x), list_names)
    total = sum(map(lambda x:x[0]*x[1],zip(all_name_vals, range(1, len(all_name_vals)+1))))
    return total

result = total_name_scores()
print result
