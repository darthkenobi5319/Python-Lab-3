# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:12:57 2017

@author: ZHENGHAN ZHANG
"""

#ask for edge length
edgeLength=int(input('Please enter an edge length:'))
#execute the for-loop
m=edgeLength
for i in range(edgeLength+1):
    print(' '*m,'* '*i)
    m-=1