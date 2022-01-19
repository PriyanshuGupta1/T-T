# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:43:46 2022

@author: KIIT PRIYANSHU GUPTA
"""


import pandas as pd
import numpy as np
dataset=pd.read_csv("E:\T&T\T&T\data.csv")
dataset['Purchased'].replace('No', 0, inplace=True)
dataset['Purchased'].replace('Yes', 1, inplace=True)
dataset['Purchased']=dataset['Purchased'].astype('int64')
t = np.array(dataset['Country'].unique())
for n, i in enumerate(t):
    dataset['Country'].replace(i, n, inplace=True)
print(dataset.corr())
