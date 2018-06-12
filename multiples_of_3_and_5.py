# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:01:40 2018

@author: cdonovan
"""

# Python 3.5
# https://projecteuler.net/problem=1

from functools import reduce

def mult_of_n(thres, n):
    """ find multiples of n below a threhold "thres"
    """
    range1 = range(1,thres)
    return filter(lambda x:x%n==0, range1)

all_mults = [list(mult_of_n(1000, n)) for n in [3,5]]
uniq_mults = reduce(lambda x,y: list(set(x+y)), all_mults)
print(sum(uniq_mults))
    
# alternative solution
# sum(multiples of 3)+sum(multiples of 5)-sum(multiples of 15)
all_mults2 = [list(mult_of_n(1000, n2)) for n2 in [3,5,15]]
list_sum = list(map(sum, all_mults2))
print(list_sum[0]+list_sum[1]-list_sum[2])