# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 00:57:52 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=4

from itertools import product

def check_palindrome(num):
    str_num = str(num)
    if str_num==str_num[::-1]:
        return True
    else:
        return False
    
def n_digit_nums(n):
    nums_1_up = range(1, 10**n)
    all_n_nums = filter(lambda x:len(str(x))==n, nums_1_up)
    return all_n_nums

def gen_all_products(n):
    all_ns = n_digit_nums(n)
    prod1 = filter(lambda x:x[0]!=x[1], product(all_ns, all_ns))
    all_prods = map(lambda x:(x[0], x[1], x[0]*x[1]), prod1)
    all_prods2 = filter(lambda x:check_palindrome(x[2]), all_prods)
    return all_prods2

def find_max_prod(n):
    all_prods3 = gen_all_products(n)
    highest = reduce(lambda x,y:x if x[2]>y[2] else y, all_prods3)
    return highest
    
result = find_max_prod(3)
print result