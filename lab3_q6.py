# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:43:46 2022

@author: KIIT PRIYANSHU GUPTA
"""


import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\T&T\T&T\Social_Network_Ads.csv')
print(dataset)
plt.title('Social Networks')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.scatter(dataset['Age'],dataset['EstimatedSalary'])
plt.show()