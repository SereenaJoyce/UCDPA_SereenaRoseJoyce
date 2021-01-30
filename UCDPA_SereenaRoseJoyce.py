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


