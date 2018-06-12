# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:31:18 2018

@author: cdonovan
"""

# Python 3.5
# https://projecteuler.net/problem=2

def fibon(n):
    """ return the nth. Fibonacci number
    """
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibon(n-1)+fibon(n-2)
    
num=1
fib_list = []
while fibon(num)<4000000:
    if fibon(num)%2==0:
        fib_list.append(fibon(num))
    num+=1
print(sum(fib_list))