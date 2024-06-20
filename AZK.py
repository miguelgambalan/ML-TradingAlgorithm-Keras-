import QuantLib as ql
import json
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

#Import Model Packages for reinforcement learning
from keras import layers
from keras import ops
from keras import backend as K
from collections import namedtuple, deque

def getDataQuote(symbol):
    apiUrl = f"https://api.twelvedata.com/quote?symbol=" + symbol + "&apikey=" + ApiKey
    response = requests.get(apiUrl)
    
    if response.status_code == 200:
        data = response.json()
        print("Full JSON response:\n", json.dumps(data, sort_keys=True, indent=4))
    else:
        print(f"Error: {response.status_code}")


def getDataMACD(symbol):
    apiUrl = f"https://api.twelvedata.com/macd?symbol=" + symbol + "&interval=1min&apikey=" + ApiKey
    response = requests.get(apiUrl)
    
    if response.status_code == 200:
        data = response.json()
        print("Full JSON response:\n", json.dumps(data, sort_keys=True, indent=4))
    else:
        print(f"Error: {response.status_code}")


#TEST ---------------------------

def main():

    getDataMACD("AMD")

    today = ql.Date(10,5,2024)

    ql.Settings.instance().evaluationDate = today


    print(ql.Settings.instance().evaluationDate)


    rate = ql.InterestRate(0.05, ql.Actual360(), ql.Compounded, ql.Annual)


    print (rate)


#TEST------------------------------
    
if __name__ == '__main__':
    main()