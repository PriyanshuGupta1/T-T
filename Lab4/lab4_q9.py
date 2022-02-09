# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:21:17 2022

@author: PRIYANSHU GUPTA
"""
n = int(input('Enter n: '))
a, b = 0, 1
if n == 1:
    print(a)
elif n == 2:
    print(a, b)
else:
    print(a, b, end=' ')
    for i in range(n-2):
        a, b = b, a+b
        print(b, end=' ')