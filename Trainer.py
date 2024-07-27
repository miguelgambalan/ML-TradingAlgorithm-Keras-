from IPython.core.debugger import set_trace
import pandas as pd
import numpy as np
import keras
from AZK import X_train
from Helper import formatPrice, getState, plot_behavior
from agent import Agent
import tensorflow

window_size = 1
agent = Agent(window_size)
#In this step we feed the closing value of the stock price 
data = X_train
l = len(data) - 1
batch_size = 32
#An episode represents a complete pass over the data.
episode_count = 1

for e in range(episode_count + 1):
    print("Running episode " + str(e) + "/" + str(episode_count))
    state = getState(data, 0, window_size + 1)
    #set_trace()
    total_profit = 0
    agent.inventory = []
    states_sell = []
    states_buy = []
    for t in range(l):
        action = agent.act(state)    
        # sit
        next_state = getState(data, t + 1, window_size + 1)
        reward = 0

        if action == 1: # buy
            agent.inventory.append(data[t])
            states_buy.append(t)
            print("Buy: " + formatPrice(data[t]))

        elif action == 2 and len(agent.inventory) > 0: # sell
            bought_price = agent.inventory.pop(0)      
            reward = max(data[t] - bought_price, 0)
            total_profit += data[t] - bought_price
            states_sell.append(t)
            print("Sell: " + formatPrice(data[t]) + " | Profit: " + formatPrice(data[t] - bought_price))

        done = True if t == l - 1 else False
        #appends the details of the state action etc in the memory, which is used further by the exeReply function
        agent.memory.append((state, action, reward, next_state, done))
        state = next_state

        if done:
            print("--------------------------------")
            print("Total Profit: " + formatPrice(total_profit))
            print("--------------------------------")
            #set_trace()
            print (agent.memory)
            dtype = [
            ('field1', 'O'),   # Object type for array
            ('field2', 'i4'),  # 4-byte integer
            ('field3', 'i4'),  # 4-byte integer
            ('field4', 'O'),   # Object type for array
            ('field5', 'b')    # Boolean
                    ]
            
            plot_behavior(data,states_buy, states_sell, total_profit)

            np.ndarray(shape=(0,5), dtype=dtype, order='F')
            structured_array = np.array(agent.memory, dtype=dtype)
            reshaped_memory = []
            for mem in structured_array:
                field1_flattened = mem['field1'].flatten()
                field4_flattened = mem['field4'].flatten()
                combined = np.concatenate([field1_flattened, [mem['field2']], [mem['field3']], field4_flattened, [mem['field5']]])
                reshaped_memory.append(combined)

            reshaped_memory = np.array(reshaped_memory)

            pd.DataFrame(reshaped_memory).to_csv("Agent"+str(e)+".csv")
            #Chart to show how the model performs with the stock goin up and down for each 
            #plot_behavior(data,states_buy, states_sell, total_profit)
        if len(agent.memory) > batch_size:
            agent.expReplay(batch_size)    
            

    #if e % 2 == 0:
    agent.model.save("model_ep" + str(e)+".keras")