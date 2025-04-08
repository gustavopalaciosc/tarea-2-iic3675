import matplotlib.pyplot as plt
from time import sleep

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
        return self.v_values[initial_state]
    

    def get_optimal_policie(self, state):
        actions = self.problem.get_available_actions(state)
        action_values = {}
        for action in actions:
            action_value = 0
            transitions = self.problem.get_transitions(state, action)
            for prob, next_state, r in transitions:
                action_value += prob * (r + self.gamma * self.v_values[next_state])
            action_values[action] = round(action_value, 5)
        if action_values:
            a = max(action_values.values())
            print(f"Estado {state}")
            for i in action_values:
                if action_values[i] == a:
                    print(f"{i}")
            sleep(1)
            print("\n")
            return max(action_values, key=action_values.get)
        else:
            return 0

            
        
    

    def get_optimal_policies(self):
        values = {}
        for state in self.problem.states:
            values[state] = self.get_optimal_policie(state)
    
        llaves = list(values.keys())
        valores = list(values.values())

    # Usamos scatter para dibujar puntos
        plt.scatter(llaves, valores, color='blue')  # Puedes cambiar el color si quieres

        plt.xlabel('Llaves')
        plt.ylabel('Valores')
        plt.title('Gráfico de apuestas óptimas')
        plt.grid(True)

    # Guardamos el gráfico en la raíz del proyecto
        plt.savefig('grafico_optimo.png')



                


    

