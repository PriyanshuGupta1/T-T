# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:49:26 2022

@author: KIIT PRIYANSHU GUPTA
"""

import pandas as pd
dataset=pd.read_csv("E:\T&T\T&T\data.csv")
country_data = {}
n = len(dataset["Country"])
for i in range(0,n):
    country=dataset["Country"][i]
    if country not in country_data:
        country_data[country] = {"Purchased":0, "Not Purchased":0}
    if dataset["Purchased"][i] == "Yes":
        country_data[country]["Purchased"] = country_data[country]["Purchased"] + 1
    elif dataset["Purchased"][i] == "No":
        country_data[country]["Not Purchased"] = country_data[country]["Not Purchased"] + 1
dataset2 = pd.DataFrame(country_data).T
print(dataset2,"\n")
