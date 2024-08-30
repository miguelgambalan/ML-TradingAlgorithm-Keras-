import json
import os
import math
import numpy as np
import pandas as pd
import requests
from userspecificdata import ApiKey
import matplotlib.pyplot as plt
from pandas import read_csv, set_option
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import datetime
import tensorflow as tf
import warnings
import keras
from keras import layers
from keras import ops
from keras import backend as K
from collections import namedtuple, deque


#to help libraries work properly
warnings.filterwarnings("ignore")
dataset = read_csv('SP500.csv',index_col=0)
type(dataset)



#dataset output for graph, table and other info
dataset.shape
set_option("display.width" , 100)
pd.options.display.max_rows = 5
pd.set_option("display.precision" , 3)
print(type(dataset))
#Gives statistics on dataset
print(dataset.describe())
dataset["Close"].plot()
plt.title("S&P 500 Closing Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()

#Cleaning data of null values
print('Null Values =',dataset.isnull().values.any())
dataset=dataset.ffill()
dataset.head(2)

X=list(dataset["Close"])
X=[float(x) for x in X]
validation_size = 0.2
train_size = int(len(X) * (1-validation_size))
X_train, X_test = X[0:train_size], X[train_size:len(X)]



