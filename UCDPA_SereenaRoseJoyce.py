print('Hello and welcome to my project')

import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# API
api = requests.get('http://api.open-notify.org/astros.json')
print(api.text)
