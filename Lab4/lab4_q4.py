# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:31:59 2022

@author: PRIYANSHU GUPTA
"""

girls=[]
boys=[]
for i in ['A', 'B', 'C']:
    f=int(input(f"Enter Number of girl in section {i}:"))
    girls.append(f)
for i in ['A', 'B', 'C', 'D', 'E']:
    f=int(input(f"Enter Number of boys in section {i}:"))
    boys.append(f)
print(f"Total number of boys: {sum(boys)}")
print(f"Total number of girls: {sum(girls)}")
print(f"Total number of students: {sum(boys)+sum(girls)}")