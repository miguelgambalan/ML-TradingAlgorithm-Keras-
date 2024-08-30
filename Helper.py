import time
from matplotlib import pyplot as plt
import numpy as np
import math
import os

# prints formatted price
def formatPrice(n):
    return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))

# returns the sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# returns an n-day state representation ending at time t
def getState(data, t, n):    
    d = t - n + 1
    if d >= 0:
        block = data[d:t + 1]
    else:
        block = [data[0]] * (-d) + data[0:t + 1]  # pad with the first element of data

    print(f"Block: {block}")  # Debugging print statement

    res = []
    for i in range(n - 1):
        print(f"block[{i + 1}] = {block[i + 1]}, block[{i}] = {block[i]}")  # Debugging print statement
        res.append(sigmoid(block[i + 1] - block[i]))
    
    return np.array([res])

# Plots the behavior of the output
def plot_behavior(data_input, states_buy, states_sell, profit):
    output_dir = 'output/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fig = plt.figure(figsize = (15,5))
    plt.ion()
    plt.plot(data_input, color='r', lw=2.)
    plt.plot(data_input, '^', markersize=10, color='m', label = 'Buying signal', markevery = states_buy)
    plt.plot(data_input, 'v', markersize=10, color='k', label = 'Selling signal', markevery = states_sell)
    plt.title('Total gains: %f'%(profit))
    plt.xlabel("# of Days")
    plt.ylabel("Price in $")
    plt.legend()
    plt.savefig('output/'+"name"+'.png')
    plt.show()
    time.sleep(10)
    plt.close()

# Example usage of getState
data = [1283.27002, 1283.27002, 1284.27002, 1285.27002, 1286.27002]  # Example list
t = 3
n = 2

state = getState(data, t, n)
print(state)
