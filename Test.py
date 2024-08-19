from datetime import date
import tensorflow
from matplotlib.mlab import window_none
from AZK import X_test
from Helper import formatPrice, getState, plot_behavior
from agent import Agent
from Trainer import episode_count

# Initialize parameters
episode_count = int(episode_count)
test_data = X_test
l_test = len(test_data) - 1
window_size = int(window_none(episode_count)) + 1  # This determines the size of the state space
state_size = window_size-1  # Set state_size to window_size

# Prepare the initial state
state = getState(test_data, 0, window_size)
total_profit = 0
is_eval = True
done = False
states_sell_test = []
states_buy_test = []

# Load the trained model
model_name = "model_ep" + str(episode_count)
agent = Agent(state_size=state_size, is_eval=is_eval, model_name=model_name + ".keras")
agent.inventory = []

for t in range(l_test):
    action = agent.act(state)
    
    next_state = getState(test_data, t + 1, window_size)
    reward = 0

    if action == 1:  # Buy
        agent.inventory.append(test_data[t])
        states_buy_test.append(t)
        print(f"Buy: {formatPrice(test_data[t])}")

    elif action == 2 and len(agent.inventory) > 0:  # Sell
        bought_price = agent.inventory.pop(0)
        reward = max(test_data[t] - bought_price, 0)
        total_profit += reward
        states_sell_test.append(t)
        print(f"Sell: {formatPrice(test_data[t])} | profit: {formatPrice(reward)}")

    done = (t == l_test - 1)
    # Append to memory only if needed, here in eval mode it is redundant
    # agent.memory.append((state, action, reward, next_state, done))
    state = next_state

    if done:
        print("------------------------------------------")
        print(f"Total Profit: {formatPrice(total_profit)}")
        print("------------------------------------------")

# Plot results
plot_behavior(test_data, states_buy_test, states_sell_test, total_profit)
