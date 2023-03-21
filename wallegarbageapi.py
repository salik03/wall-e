import numpy as np
from flask import Flask, request

app = Flask(__name__)

class QLearningAgent:
    def __init__(self, alpha, gamma, epsilon, n_states, n_actions):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_states = n_states
        self.n_actions = n_actions
        self.Q = np.zeros((n_states, n_actions))

    def choose_action(self, state):
        if np.random.uniform() < self.epsilon:
            return np.random.choice(self.n_actions)
        else:
            return np.argmax(self.Q[state, :])

    def update(self, state, action, reward, next_state):
        self.Q[state, action] = (1 - self.alpha) * self.Q[state, action] + \
                                self.alpha * (reward + self.gamma * np.max(self.Q[next_state, :]))

    def save(self, filename):
        np.save(filename, self.Q)

    def load(self, filename):
        self.Q = np.load(filename)

# Create Q-learning agent
alpha = 0.1
gamma = 0.9
epsilon = 0.1
n_states = 4
n_actions = 1
agent = QLearningAgent(alpha, gamma, epsilon, n_states, n_actions)

# Create dictionary of disposal station coordinates
disposal_coords = {
    'Biodegradable': (75.1, -4.6, -349.5),
    'Recyclable': (12.9, -4.6, -331.9),
    'Hazardous': (159.4, -4.6, -299.2)
}

# Define route for training bot
@app.route('/train/<float:x>/<float:y>/<float:z>/<string:category>/<int:capacity>', methods=['POST'])
def train(x, y, z, category, capacity):
    # Determine current state based on category and coordinates
    if capacity < 20:
        state = list(disposal_coords[category])
    else:
        state = [x, y, z]

    # Choose action
    action = agent.choose_action(state)

    # Determine next state based on action
    if capacity < 20:
        next_state = list(disposal_coords[max(set(agent.Q[state, :]), key = agent.Q[state, :].count)])
    else:
        next_state = [np.random.uniform(-200, 200), 0.5, np.random.uniform(-200, 200)]

    # Update Q-values
    agent.update(state, action, reward, next_state)

    # Choose next action
    next_action = agent.choose_action(next_state)

    # Return next coordinates
    return ','.join([str(x) for x in next_state])

# Define route for saving bot
@app.route('/save', methods=['GET'])
def save():
    # Save Q-table to file
    agent.save('bot.npy')
    return 'Bot saved successfully!'

# Define route for loading bot
@app.route('/load', methods=['GET'])
def load():
    # Load saved Q-table from file
    agent.load('bot.npy')
    return 'Bot loaded successfully!'

if __name__ == '__main__':
    app.run()