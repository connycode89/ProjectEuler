# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:30:52 2018

@author: jdonovc
"""

import itertools

def gen_3_dig_nums():
    nums = '0123456789'
    prod = itertools.product(list_nums0, repeat=3)
    filt = filter(lambda x:x[0]!='0',prod)
    all_nums = list(map(lambda x:int(x[0]+x[1]+x[2]),filt))
    return all_nums

def check_pal(num):
    num2 = str(num)
    if num2==num2[::-1]:
        return True
    else:
        return False
    
nums3 = gen_3_dig_nums()
products = map(lambda x:x[0]*x[1],itertools.product(nums3, repeat=2))
pals = filter(lambda x:check_pal(x), products)
print(max(list(pals)))