# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:39:24 2022

@author: KIIT PRIYANSHU GUPTA
"""

import pandas as pd
dataset=pd.read_csv("E:\T&T\T&T\data.csv")

print('\nDataset:\n')
print(dataset)
dataset1=dataset.copy(deep=False)
print('\nNew Dataset with shallow copy\n')
print(dataset1)