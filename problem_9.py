# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 01:37:45 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=9

from itertools import product

def check_pythag(a, b, c):
    if a**2+b**2 == c**2:
        return True
    else:
        return False
    
def check_sum(a, b, c):
    if a+b+c==1000:
        return True
    else:
        return False
    
# want the following condition to hold...
# ab-1000*(a+b-500) = 0
def gen_abs():    
    a_list, b_list = range(1,500), range(1,500)
    prod = product(a_list, b_list)
    prod2 = filter(lambda x:x[0]<x[1],prod)
    map1 = map(lambda x:(x[0], x[1], (x[0]**2+x[1]**2)**0.5), prod2)
    return map1

def filt_abs():
    list_abs = gen_abs()
    filt1 = filter(lambda x:x[0]*x[1]-1000*(x[0]+x[1]-500)==0, list_abs)[0]
    return filt1

def prod(a, b, c):
    prod1 = a*b*c
    return int(prod1)

abc_tuple = filt_abs()
# check that this tuple satisfies the 2 conditions (a^2+b^2 = c^2 and a+b+c=1000)
print check_pythag(*abc_tuple)
print check_sum(*abc_tuple)
# print final answer
print prod(*abc_tuple)