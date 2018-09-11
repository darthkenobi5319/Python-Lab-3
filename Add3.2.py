# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:39:05 2017

@author: ZHENGHAN ZHANG
"""
from functools import reduce
#define the sentence
s = 'The rain in Spain falls mainly on the plain'

#Reverse
print(reduce((lambda x,s:x+s),list(s)[::-1]))
#count
print(sum(map((lambda x:1),range(len(s)))))
#single character count
print(sum(map((lambda x: x=='a'),list(s))))
#upper
x=''
x=x.join(map((lambda x: x.upper()),list(s)))
print(x)