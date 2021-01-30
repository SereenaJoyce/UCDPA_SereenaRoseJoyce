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


# Creating dictionaries
dictionary1 = {'movie_name':['A Holiday Engagement','A Home with a View','A House of Blocks','A kid from Coney Island','A Kind of Murder','A Korean Odyssey', 'A Land Imagined','A Leaf of faith','A Life of Speed:The Juan manual Fangio Story','A Lion in the House'],
               'rating':['TV-G','TV-MA','TV-PG','TV-MA','R','TV-MA','TV-MA','TV-MA','TV-14','TV-14']}

df1=pd.DataFrame(dictionary1)
print(df1)


dictionary2 = {'movie_name':['A Holiday Engagement','A Home with a View','A House of Blocks','A kid from Coney Island','A Kind of Murder', 'A Korean Odyssey','A Land Imagined','A Leaf of Faith','A Life of Speed:The Juan manual Fangio Story','A Lion in the House'],
               'release_year':['2011','2019','2017','2019','2016','2017','2019','2018','2020','2006']}

df2=pd.DataFrame(dictionary2)
print(df2)


# Merging DataFrames
merged_data=df1.merge(df2, on='movie_name')
print(merged_data)





