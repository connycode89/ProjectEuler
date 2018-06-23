# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 01:41:36 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=24

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

def generate_list(n):
    return range(0, n+1)

def find_nth_permutation(n, n2):
    """ given digits from 0 to n2, order the (n2+1)! permutations and find the nth one in the list
    """
    k = n-1
    digit_list = []
    nums_list = generate_list(n2)
    while len(nums_list)!=0:   
        divide, k = k/factorial(n2), k%factorial(n2)
        digit_list.append(nums_list[divide])
        nums_list = [p for p in nums_list if p!=nums_list[divide]]
        n2-=1
    digs1 = ''.join(map(lambda x:str(x), digit_list))
    return digs1

result = find_nth_permutation(1000000, 9)
print result