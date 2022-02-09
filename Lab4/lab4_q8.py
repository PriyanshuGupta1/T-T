# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:21:17 2022

@author: PRIYANSHU GUPTA
"""
n=int(input('Enter number:'))
c=0
for i in range(2, n):
    if n%i == 0:
        c += 1
        break
if c!=0:
    print('The Number is not prime')
else:
    print('The Number is Prime')