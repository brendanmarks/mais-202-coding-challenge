# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:55:32 2018

MAIS 202 CODING PROBLEM
@author: Brendan
"""

import csv
from matplotlib import pyplot as plt
import pandas as pd


def createCategories():
    categories = {}
    for row in reader:
        name = row[16]
        if name not in categories:
            categories[name] = ""
    return categories 

def getAverages(dict):
    for category in dict_categories.keys():
        total = 0
        count = 0
        f.seek(0)
        for row in reader:
            if row[16] == category:
                total += float(row[5])
                count += 1
        try:
            dict_categories[category] = total / count
        except ZeroDivisionError:
            pass
        
    
   
   
filepath = ("C:/Users/Brendan/Documents/data.csv") 
with open(filepath) as f:
    reader = csv.reader(f)
   
    header_row = next(reader)
    
    dict_categories = {}
    dict_categories = createCategories()
    getAverages(dict_categories)





df = pd.DataFrame(list(dict_categories.items()), columns=['Purpose','Avg Rate']) #dict_categories, orient="index") #, index['Purpose','Average Rate']) 

print(df)




colors = ['red', 'blue', 'navy','lime']
plt.bar(dict_categories.keys(), dict_categories.values(), color=colors)
plt.xticks(rotation='vertical')
plt.xlabel('Purpose', fontsize=10)
plt.ylabel('Average Rates', fontsize=10)
plt.title('Purpose to Average Rate Chart')
plt.show()