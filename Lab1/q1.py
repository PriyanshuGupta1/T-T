# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:29:22 2022

@author: Priyanshu Gupta
"""
def age_convert(val):
    val_converted=val/12
    return val_converted

import pandas as pd
dataset=pd.read_csv("E:\T&T\TnT\Lab1\data.csv")
sal_class=[]
j=0
while j<10:
    sal=dataset['Salary'][j]
    if sal>70000:
        sal_class.append('class0')
    elif sal>=61000:
        sal_class.append('class1')
    elif sal >= 48000:
        sal_class.append('class2')
    else:
        sal_class.append('')
    j+=1
dataset['Salary_class']=sal_class
count0 = len(dataset[dataset['Salary_class']=='class0'])
count1 = len(dataset[dataset['Salary_class']=='class1'])
count2 = len(dataset[dataset['Salary_class']=='class2'])
print("count1="+str(count1))

dataset['Age_Converted'] = age_convert(dataset['Age'])
print(dataset)

