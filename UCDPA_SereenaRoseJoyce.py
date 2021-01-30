print('Hello and welcome to my project')

import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# API
api = requests.get('http://api.open-notify.org/astros.json')
print(api.text)

# importing a csv file
data=pd.read_csv('netflix_titles.csv', index_col=0)
print(data.head())
print(data.shape)
print(data.columns)

# Functions that create reusable code
def functioncl():
    print('The number of movies and TV shows release each year is')
    print(filled_data['release_year'].value_counts(sort=True))

def functioncl2():
    print('Now, off we go to play with dictionaries ')

def functioncl3():
    print('Using numbers to illustrate numpy and if loop')


# Sorting data
sorted_data = data.sort_values('release_year',ascending=False)
print(sorted_data[['release_year','title']])


# To count the missing values in each column
missing_values=data.isna().sum()
print(missing_values)

# shows data with 0 replaced for null values
filled_data = data.fillna(0)
print(filled_data)

# counting to check
counting_to_check=filled_data.isna().sum()
print(counting_to_check)


# iterrows
for lab, row in filled_data.iterrows():
    print(lab + ':' + row['title'])

functioncl()

functioncl2()





