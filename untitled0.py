# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:40:49 2022

@author: KIIT
"""
import pandas as pd

import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_csv("E:\T&T\T&T\data.csv")
df
print(pd)
plt.xlabel('salary')
plt.ylabel('Age')
plt.scatter(df.Salary,df.Age,color='red',marker='+')
reg=linear_model.LinearRegression()
#creating an object of lInear regression
reg.fit(df[['salary']],df.price)
#training the data model with available data points
#data frame is given as argument