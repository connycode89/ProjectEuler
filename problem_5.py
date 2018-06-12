# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 00:25:17 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=5

import math

def check_divisibility(num1, num2):
    if num1%num2==0:
        return True
    else:
        return False
    
def check_list(num3, list1):
    list2 = map(lambda x:check_divisibility(num3, x), list1)
    check = sum(list2)==len(list2)
    return check

def find_prime_factors(num1):
    list_primes = []
    while num1%2==0:
        list_primes.append(2)
        num1/=2
    for i in range(3, int(math.sqrt(num1))+1, 2):
        while num1%i==0:
            list_primes.append(i)
            num1/=i
    if num1>2:
        list_primes.append(num1)
    return list_primes

def find_prime_factors_all(list2):
    map1 = map(lambda x:find_prime_factors(x), list2)
    return map1

def find_unique_primes(list3):
    uniques = list(reduce(lambda x, y: set(x).union(set(y)), find_prime_factors_all(list3)))
    return uniques

def lcm_factors(list4):
    prime_list = find_prime_factors_all(list4)
    uniq_primes = find_unique_primes(list4)
    dict1 = {}
    for num in uniq_primes:
        dict1[num] = max(map(lambda x: x.count(num), prime_list))
    return dict1

def calc_lcm(list5):
    num2 = 1
    facts = lcm_factors(list5)
    for key in facts:
        num2*=key**facts[key]
    return num2
        
final_answer = calc_lcm(range(1,21))
print final_answer, check_list(final_answer, range(1,21))