# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:38:17 2022

@author: PRIYANSHU GUPTA
"""

num=int(input('Enter number:'))
factorial = 1
if num < 0:
   print("Factorial of the number is not defined")
elif num==0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   