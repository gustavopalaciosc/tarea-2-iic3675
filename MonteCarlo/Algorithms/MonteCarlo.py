import random
from time import sleep
#from ..Environments.AbstractEnv import AbstractEnv

class MonteCarloControl:
    def __init__(self, env, gamma, epsilon, num_episodes):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_episodes = num_episodes
        self.q_values = {}
        self.n_returns = {}



   

    def get_optimal_action(self, state, actions):
        q_lookup = lambda a: self.q_values.get((state, a), 0)
        return max(actions, key=q_lookup)


    def run_rollout(self):
        trace = []
        state = self.env.reset()
        done = False
        
        while not done:
            #sleep(0.125)
            #print(current_state)
            if random.random() < self.epsilon:
                action = random.choice(self.env.action_space)
            else:
                action = max(self.env.action_space, key=lambda action: self.q_values.get((state, action), 0))

            next_state, reward, done = self.env.step(action)
            trace.append([state, action, reward])
            state = next_state
            
        return trace
    

    def run_greedy_policy(self):
        state = self.env.reset()
        done = False

        while not done:
            self.env.show()
            action = self.get_optimal_action(state, self.env.action_space)
            next_state, reward, done = self.env.step(action)
            state = next_state
            
            
        

    def run_montecarlo(self):
        v_initial_state = []
        for episode in range(self.num_episodes):
            trace = self.run_rollout()
            g = 0

            for state, action, reward in trace[::-1]:
                g = reward + self.gamma * g
                
                if (state, action) not in self.q_values:
                    self.q_values[(state, action)] = 0
                    self.n_returns[(state, action)] = 0

                self.n_returns[(state, action)] += 1
                self.q_values[(state, action)] += (g - self.q_values[(state, action)]) / self.n_returns[(state, action)]
            
            v_initial_state.append(g)
            if episode % 1000 == 0:
                print(f"Ep. {episode}. Current return: {g:0.3f}. Avg return: {sum(v_initial_state)/len(v_initial_state):0.3f}")


        for state_action in self.q_values:
            print(f"{state_action}: {self.q_values[state_action]}")
        print(len(self.q_values))

        self.run_greedy_policy()