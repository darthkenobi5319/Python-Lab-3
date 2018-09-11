# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:52:09 2017

@author: ZHENGHAN ZHANG
"""

#define the string and the vowels
myString = 'The quiCk brOwn fOx jumped over thE lAzy dog'
vowels=['a','e','i','o','u']
#count the numbers
n=0
for i in vowels:    
    for m in myString:
        n+= int(i==m.lower())
print('There are',n,'vowels in the sentence.')