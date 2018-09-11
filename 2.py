# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:03:11 2017

@author: ZHENGHAN ZHANG
"""
#define the string
s = 'The rain in Spain falls mainly on the plain'
#count the characters in string
x=0
for i in s:
    x+=1
print(x)
#making a replica
x=''
for i in s:
    x+=i
print(x)
#reverse
t=''
for i in range(len(s)-1,-1,-1):
    t+=s[i]
print(t)
#UpperCase
v=''
for i in s:
    v+=i.upper()
print(v)
#count c
c='a'
m=0
for i in range(len(s)):
    m+=(c==s[i])
print(m)
#generalized counting
c2='ain'
n=0
for i in range(len(s)):
    n+=(c2==s[i:i+3])
print(n)