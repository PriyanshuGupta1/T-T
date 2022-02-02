# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:09:10 2022

@author: PRIYANSHU GUPTA
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv("E:\T&T\TnT\Lab3\Data.csv")
print(dataset)
counts=[3,3,3]
Country=('France','Spain','Germany')
index=np.arange(len(Country))
plt.bar(index,counts,color=['green','yellow','blue'])
plt.xticks(index,Country,rotation=0)
plt.title('Barplot of Country')
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.show()
