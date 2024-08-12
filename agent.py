import os
import random
import numpy as np
from collections import deque
import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import adam_v2

class Agent:
    def __init__(self, state_size, is_eval=False, model_name=""):
        self.state_size = state_size
        self.action_size = 3
        self.memory = deque(maxlen=1000)
        self.inventory = []
        self.model_name = model_name
        self.is_eval = is_eval

        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        
        if self.is_eval:
            self.model = load_model(model_name)
        else:
            self.model = self._model()

    def _model(self):
        # Define input layer
        inputs = Input(shape=(self.state_size,))  # Adjust state_size to match your input dimension
        
        # Add hidden layers
        x = Dense(units=64, activation='relu')(inputs)
        x = Dense(units=32, activation='relu')(x)
        x = Dense(units=8, activation='relu')(x)
        
        # Define output layer
        outputs = Dense(self.action_size, activation='linear')(x)  # Adjust action_size to match your output dimension
        
        # Create the model
        model = Model(inputs=inputs, outputs=outputs)
        
        # Configure the optimizer
        optimizer = adam_v2.Adam(learning_rate=0.001)
        
        # Compile the model
        model.compile(optimizer=optimizer, loss='mse')  # type: ignore
        
        return model
    
    def act(self, state):
        if not self.is_eval and np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        options = self.model.predict(state)
        return np.argmax(options[0])

    def expReplay(self, batch_size):
        mini_batch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in mini_batch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
