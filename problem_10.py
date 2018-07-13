# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 01:51:43 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=10

# using a function from here
# https://codegolf.stackexchange.com/questions/6309/list-of-first-n-prime-numbers-most-efficiently-and-in-shortest-code
def sieve():
    # Sieve of Eratosthenes
    n = 15485864  
    a, x = [1]*n, xrange
    for i in x(2, 3936):
        if a[i]:
            for j in x(i*i, N, i):
                a[j] = 0
    primes = [i for i in x(len(a)) if a[i]==1][2:]
    return primes  

def primes_below_n(n1):
    primes2 = sieve()
    primes_n1 = filter(lambda x:x<n1, primes2)
    return primes_n1

def sum_primes(list1):
    return sum(list1)

def get_sum(n2):
    primes3 = primes_below_n(n2)
    summer = sum_primes(primes3)
    return summer

result = get_sum(2000000)
print result