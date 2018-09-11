# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:14:18 2017

@author: ZHENGHAN ZHANG
"""
from functools import reduce
import random

#get the list from the user
x=list(map(lambda x: int(x), input('Please enter a string of numbers: ').split()))
#produce a new list with the results
print(list(map(lambda i: reduce(lambda x,y: x+y ,x[:i+1]),range(len(x)))))




#randomize a string of numbers with random amount of numbers from 10**3 to 10**4
x=list(map(lambda x: random.randrange(10**3,10**4), range(random.randrange(10**3,10**4))))
print(x)
print(list(map(lambda i: reduce(lambda x,y: x+y ,x[:i+1]),range(len(x)))))

#for map(f,x) and reduce(f,x), x cannot be integer: use range()