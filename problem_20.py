# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:59:34 2018

@author: jdonovc
"""

# Python 2.7
# https://projecteuler.net/problem=20

num2 = 1
for num in range(1,101):
    print num
    num2*=num
num3 = 0
for item in str(num2):
    num3+=int(item)