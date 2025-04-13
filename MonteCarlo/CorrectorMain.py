from Environments.CliffEnv import CliffEnv
from Environments.BlackjackEnv import BlackjackEnv
from Algorithms.MonteCarlo import MonteCarloControl


class CorrectorMain:
    def __init__(self):
        self.num_episodes = None
        self.epsilon = None
        self.gamma = 1.0
        self.algorithm = None


    def select_num_episodes(self):
        print("""
ELECCIÓN NÚMERO DE EPISODIOS
""")    
        num_episodes = int(input("Ingrese número de episodios: "))
        self.num_episodes = num_episodes
        return 
    

    def select_epsilon(self):
        print("""
ELECCIÓN VALOR EPSILON
""")    
        epsilon = float(input("Ingrese valor de epsilon: "))
        self.epsilon = epsilon
        return
        

    def run(self):
        pass
        







if __name__ == "__main__":
    env = CliffEnv(width=6)
    #env = BlackjackEnv()
    
    num_episodes = 200000
    epsilon = 0.1
    gamma = 1.0

    exp = MonteCarloControl(env=env, gamma=gamma, epsilon=epsilon, num_episodes=num_episodes)
    exp.run_montecarlo()

    