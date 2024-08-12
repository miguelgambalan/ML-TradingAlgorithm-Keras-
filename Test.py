#agent is already defined in the training set above.
from datetime import date
import tensorflow
from matplotlib.mlab import window_none
from AZK import X_test
from Helper import formatPrice, getState, plot_behavior
from agent import Agent
from Trainer import episode_count

episode_count = int(episode_count)
test_data = X_test
l_test = len(test_data) - 1
state = getState(test_data, 0, window_none(episode_count) + 1)
total_profit = 0
is_eval = True
done = False
states_sell_test = []
states_buy_test = []
#Get the trained model
model_name = "model_ep"+str(episode_count)
agent = Agent(window_none, is_eval, model_name + ".keras")
state = getState(date, 0, window_none(episode_count) + 1)
total_profit = 0
agent.inventory = []

for t in range(l_test):
    action = agent.act(state)
    print(action)
    #set_trace()
    next_state = getState(test_data, t + 1, window_none(episode_count) + 1)
    reward = 0

    if action == 1:
        agent.inventory.append(test_data[t])
        states_buy_test.append(t)
        print("Buy: " + formatPrice(test_data[t]))

    elif action == 2 and len(agent.inventory) > 0:
        bought_price = agent.inventory.pop(0)
        reward = max(test_data[t] - bought_price, 0)
        #reward = test_data[t] - bought_price
        total_profit += test_data[t] - bought_price
        states_sell_test.append(t)
        print("Sell: " + formatPrice(test_data[t]) + " | profit: " + formatPrice(test_data[t] - bought_price))

    if t == l_test - 1:
        done = True
    agent.memory.append((state, action, reward, next_state, done))
    state = next_state

    if done:
        print("------------------------------------------")
        print("Total Profit: " + formatPrice(total_profit))
        print("------------------------------------------")
        
plot_behavior(test_data,states_buy_test, states_sell_test, total_profit)