# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:15:15 2022

@author: KIIT PRIYANSHU GUPTA
"""
import pandas as pd
dataset=pd.read_csv("E:\T&T\T&T\data.csv")

print(dataset['Country'].value_counts())