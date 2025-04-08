from time import sleep

class IterativePolicyIteration:
    def __init__(self, gamma, problem, threshold = 0.0000000001):
        self.problem = problem
        self.threshold = threshold
        self.gamma = gamma
        self.v_values = dict.fromkeys(problem.states, 0.0)

    
    def run_uniform_policy(self):
        while True:
            error = 0
            for s in self.v_values:
                actions = self.problem.get_available_actions(s)
                num_actions = len(actions)
                v = self.v_values[s]
                new_v = 0
                for action in actions:
                    if self.problem.is_terminal(s): 
                        continue
                    for prob, next_s, r in self.problem.get_transitions(state = s, action=action):
                        new_v += prob * (1 / num_actions) * (r + self.gamma * self.v_values[next_s])
                self.v_values[s] = new_v
                error = max(error, abs(v - self.v_values[s]))
            
            if error < self.threshold:
                break
    


    def get_initial_state_value(self):
        return self.v_values[self.problem.get_initial_state()]
    

    def run_greedy_policy(self):
        while True:
            error = 0
            for s in self.v_values:
                actions = self.problem.get_available_actions(s)
                v = self.v_values[s]
                new_v = 0
                aux = 0
                
                if self.problem.is_terminal(s): 
                        continue
                
                greedy_a = self.get_greedy_actions(s)
                for action in actions:
                    if action in greedy_a:
                        for prob, next_s, r in self.problem.get_transitions(state = s, action=action):
                            aux += prob * (r + self.gamma * self.v_values[next_s])
                        new_v +=  aux
                        break
                self.v_values[s] = new_v
                error = max(error, abs(v - self.v_values[s]))
    
            if error < self.threshold:
                break


    def get_greedy_actions(self, current_state):
        actions = self.problem.get_available_actions(current_state)
        action_values = {}
        greedy_actions = []

        for action in actions:
            aux = 0
            for prob, next_s, r in self.problem.get_transitions(state = current_state, action=action):
                aux += prob * (r + self.gamma * self.v_values[next_s])
            action_values[action] = aux

        max_value = max(list(action_values.values()))
        for action in action_values:
            if action_values[action] == max_value:
                greedy_actions.append(action)

        return greedy_actions



            

    
    

