# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 01:04:15 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=12

def gen_nth_tri_num(n):
    tri = n*(n+1)/2
    return tri

def get_num_factors(num):
    sqrt = num**0.5
    nums_to_check = range(1, int(sqrt)+1)
    num_facts = 0
    for item in nums_to_check:
        if num%item==0:
            num_facts+=1
    if int(sqrt)==sqrt:
        num_facts = num_facts*2-1
    else:
        num_facts = num_facts*2
    return num_facts

def find_first_tri(threshold):
    num2 = 1
    while True:
        tri2 = gen_nth_tri_num(num2)
        num_facts2 = get_num_factors(tri2)
        if num_facts2>threshold:
            break
        else:
            num2+=1
    return num2, tri2

n = find_first_tri(500)
print "n:",n[0]
print "nth triangle number:",n[1]