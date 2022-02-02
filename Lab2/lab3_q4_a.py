# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:43:46 2022

@author: KIIT PRIYANSHU GUPTA
"""


import pandas as pd
dataset=pd.read_csv("E:\T&T\TnT\Lab2\data.csv")

dataset['Purchased'].replace('No', 0, inplace=True)
dataset['Purchased'].replace('Yes', 1, inplace=True)
dataset['Purchased']=dataset['Purchased'].astype('int64')
print(pd.crosstab(index=dataset['Purchased'],columns = dataset['Country'],
        dropna=True,normalize=True))