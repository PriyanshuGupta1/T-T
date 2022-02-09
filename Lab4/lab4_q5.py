# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:31:59 2022

@author: PRIYANSHU GUPTA
"""
import math
amount=input("Enter the amount of money:")
cost_jean=750
number_of_jean=math.floor(int(amount)/cost_jean)
additional=((number_of_jean+1)*750)-int(amount)
print("The number of jean are",number_of_jean)
print("Money needed for additional jean",additional)

