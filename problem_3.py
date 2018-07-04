# -*- coding: utf-8 -*-
"""
Created on Wed Jul 04 01:59:22 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=3

import math

# function borrowed from problem 5
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

def find_max(num2):
    prime_list = find_prime_factors(num2)
    return max(prime_list)

result = find_max(600851475143)
print result