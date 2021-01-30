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

