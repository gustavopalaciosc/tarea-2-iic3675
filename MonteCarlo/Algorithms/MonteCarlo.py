import random
from time import sleep

class MonteCarloControl:
    def __init__(self, env, gamma, epsilon, num_episodes, num_episodes_report, num_greedy_runs):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_episodes = num_episodes
        self.num_episodes_report = num_episodes_report 
        self.num_greedy_runs = num_greedy_runs 
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
            if random.random() < self.epsilon:
                action = random.choice(self.env.action_space)
            else:
                action = self.get_optimal_action(state=state, actions=self.env.action_space)

            next_state, reward, done = self.env.step(action)
            trace.append([state, action, reward])
            state = next_state
            
        return trace
    

    def run_greedy_policy(self, show):
        state = self.env.reset()
        done = False
        avg_return = 0
        for i in range(self.num_greedy_runs):
            g = 0
            while not done:
                if show:
                    self.env.show()
                action = self.get_optimal_action(state, self.env.action_space)
                next_state, reward, done = self.env.step(action)
                g += reward
                state = next_state

            avg_return += (g - avg_return) / (i + 1)
        return avg_return
            
        
    def run_montecarlo(self):
        self.q_values = {}
        self.n_returns = {}
        greedy_returns = []
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
            
            if episode % self.num_episodes_report == 0:
                if episode == 0:
                    greedy_returns.append(g)
                    print(f'Episodio {episode}. Retorno: {g}')
                else:
                    greedy_return = self.run_greedy_policy(False)
                    greedy_returns.append(greedy_return)
                    print(f'Episodio {episode}. Retorno greedy: {greedy_return}. Retorno episodio: {g}')


        for state_action, value in sorted(self.q_values.items(), key=lambda x: x[0][0]):
            print(f"{state_action}: {value}")
        #for state_action in self.q_values:
        #    print(f"{state_action}: {self.q_values[state_action]}")
        #print(len(self.q_values))

        self.run_greedy_policy(True)
        #print(self.q_values)
        return greedy_returns