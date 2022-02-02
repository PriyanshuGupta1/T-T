# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:09:10 2022

@author: PRIYANSHU GUPTA
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("E:\T&T\TnT\Lab3\Social_Network_Ads.csv")
plt.hist(dataset['EstimatedSalary'], color='blue', edgecolor='white', bins=4)
plt.xlabel('Estimated Salary')
plt.ylabel('Frequency')
plt.title('Histogram of Estimated Salary')
plt.show()