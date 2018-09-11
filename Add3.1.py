# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:35:52 2017

@author: ZHENGHAN ZHANG
"""

from functools import reduce
#Add
print(reduce((lambda x,n:x+n),range(1,11)))
#multiplication
print(reduce((lambda x,y:x*y),range(1,101)))