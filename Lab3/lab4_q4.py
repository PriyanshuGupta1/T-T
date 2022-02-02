# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:09:10 2022

@author: PRIYANSHU GUPTA
"""
import pandas as pd
import seaborn as sns

dataset=pd.read_csv("E:\T&T\TnT\Lab3\Social_Network_Ads.csv")
print(dataset)
sns.set(style="darkgrid")
sns.regplot(x=dataset['Age'],y=dataset['EstimatedSalary'])

