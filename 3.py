# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:24:15 2017

@author: ZHENGHAN ZHANG
"""

#get the list from the user
x=input('Please enter a string of numbers: ').split()
#create the sum list
v=x.copy()
m=0
print(v)
for i in range(len(x)):
    m+=int(x[i])
    v[i]=m
print(v)



#Randomize
import random
randomNumber=random.randrange(10**3,10**4)
x=[]
#create a random list of random size
for i in range(randomNumber):
    x.append(random.randrange(10**3,10**4))
print(x)
# sum
v=x.copy()
m=0
for i in range(len(x)):
    m+=x[i]
    v[i]=m
print(v)