# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 01:07:59 2018

@author: Conor
"""

# Python 2.7
# https://projecteuler.net/problem=7

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

def get_nth_prime(n1):
    primes2 = sieve()
    return primes2[n1-1]

result = get_nth_prime(10001)
print result