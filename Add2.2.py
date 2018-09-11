# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:18:48 2017

@author: ZHENGHAN ZHANG
"""

import timeit
import random

# your code block

#Define a string
string1=''
for i in range(5000):
    string1 += str(random.randrange(1,1000))
#time it
start_time = timeit.default_timer()
#use string iteration

n=[]
n.append(string1[-1])
for i in string1:
    n.append(i)
n.pop()
string=''
string=string.join(n)

print(string)

print(timeit.default_timer() - start_time)