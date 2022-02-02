# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:15:15 2022

@author: KIIT PRIYANSHU GUPTA
"""
import pandas as pd
dataset=pd.read_csv("E:\T&T\TnT\Lab2\data.csv")
print(dataset)
print(dataset['Country'].value_counts())