import QuantLib as ql
import json
import math
import numpy as np
import pandas as pd
import requests
from userspecificdata import ApiKey
from IPython.core.debugger import set_trace
import matplotlib.pyplot as plt
from pandas import read_csv, set_option
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import datetime
import tensorflow as tf
import warnings
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
print("describe")
print(dataset.describe())
dataset["Close"].plot()
plt.title("S&P 500 Closing Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()

#Cleaning data of null values
print('Null Values =',dataset.isnull().values.any())
dataset=dataset.fillna(method='ffill')
dataset.head(2)

X=list(dataset["Close"])
X=[float(x) for x in X]
validation_size = 0.2
train_size = int(len(X) * (1-validation_size))
X_train, X_test = X[0:train_size], X[train_size:len(X)]





def getDataQuote(symbol):
    apiUrl = f"https://api.twelvedata.com/quote?symbol=" + symbol + "&apikey=" + ApiKey
    response = requests.get(apiUrl)
    
    if response.status_code == 200:
        data = response.json()
        print("Full JSON response:\n", json.dumps(data, sort_keys=True, indent=4))
    else:
        print(f"Error: {response.status_code}")


def getDataMACD(symbol):
    apiUrl = f"https://api.twelvedata.com/macd?symbol=" + symbol + "&interval=1day&apikey=" + ApiKey
    response = requests.get(apiUrl)
    
    if response.status_code == 200:
        data = response.json()
        print("Full JSON response:\n", json.dumps(data, sort_keys=True, indent=4))
    else:
        print(f"Error: {response.status_code}")





#TEST ---------------------------



def main():

    #getDataMACD("AMD")

    today = ql.Date(10,5,2024)

    ql.Settings.instance().evaluationDate = today


    print(ql.Settings.instance().evaluationDate)


    rate = ql.InterestRate(0.05, ql.Actual360(), ql.Compounded, ql.Annual)


    print (rate)
    print(dataset.head(10))


#TEST------------------------------
    
if __name__ == '__main__':
    main()