

class ValueIteration:
    def __init__(self, gamma, problem, threshold = 0.0000000001):
        self.gamma = gamma
        self.problem = problem
        self.threshold = threshold
        self.v_values = dict.fromkeys(problem.states, 0.0)

    def run_value_iteration(self):
        
        while True:
            delta = 0
            for state in self.v_values:
                if self.problem.is_terminal(state):
                    continue
                v = self.v_values[state]
                self.v_values[state] = self.max_action_value(current_state=state)
                delta = max(delta, abs(v - self.v_values[state]))
            if delta < self.threshold:
                break
            
                
    def max_action_value(self, current_state):
        actions = self.problem.get_available_actions(current_state)
        action_values = []
        for action in actions:
            aux = 0
            transitions = self.problem.get_transitions(state=current_state, action=action)
            for prob, next_state, r in transitions:
                aux += prob * (r + self.gamma * self.v_values[next_state])
            action_values.append(aux)
        
        return max(action_values)
    

    def get_initial_state_value(self):
        initial_state = self.problem.get_initial_state()
        print(self.v_values)
        return self.v_values[initial_state]

                


    

