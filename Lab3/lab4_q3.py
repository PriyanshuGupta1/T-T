# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:09:10 2022

@author: PRIYANSHU GUPTA
"""
import pandas as pd

dataset=pd.read_csv("E:\T&T\TnT\Lab3\Data.csv",index_col=0)
print("The shape of dataset without droping NA values:")
print(dataset.shape)
dataset1=pd.read_csv("E:\T&T\TnT\Lab3\Data.csv",index_col=0)
dataset1.dropna(axis=0,inplace=True)
print("The shape of dataset after droping NA values:")
print(dataset1.shape)