# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:49:28 2017

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
m=string1[-1]
x=''
x += m
for i in range(1,len(string1)):
    x += string1[i-1] 
print(x)   

print(timeit.default_timer() - start_time)