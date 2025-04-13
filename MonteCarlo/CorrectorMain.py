import matplotlib.pyplot as plt
from Environments.CliffEnv import CliffEnv
from Environments.BlackjackEnv import BlackjackEnv
from Algorithms.MonteCarlo import MonteCarloControl


class CorrectorMain:
    def __init__(self):
        self.algorithm = None
        self.env = None
        self.runs = {f"Run {i}": None for i in range(1, 6)}
        self.select_env()


    def select_env(self):
        print("""
SELECCIONA EL PROBLEMA 
[1] Blackjack
[2] Cliff
""")    
        while True:
            option = input("Selecciona un problema: ")
            if option == "1":
                self.env = BlackjackEnv()
                self.algorithm = MonteCarloControl(env=self.env, 
                                                   gamma=1.0, 
                                                   epsilon=0.01, 
                                                   num_episodes=10000000, 
                                                   num_episodes_report=500000, 
                                                   num_greedy_runs=100000)
                break
            elif option == "2":
                while True:
                    try:
                        width = int(input("Ingrese ancho del ambiente Cliff: "))
                        if 12 >= width >= 6: 
                            break
                        else:
                            pass
                    except:
                        pass
                self.env = CliffEnv(width=width)
                self.algorithm = MonteCarloControl(env=self.env, 
                                                   gamma=1.0, 
                                                   epsilon=0.1, 
                                                   num_episodes=200000,
                                                   num_episodes_report=1000, 
                                                   num_greedy_runs=1)
                break
            else:
                print("Opción inválida")
                pass
        

    def run(self):
        for run in range(5):
            returns = self.algorithm.run_montecarlo()
            self.runs[f"Run {run + 1}"] = returns
            print(self.runs)


    def plot_runs(self):

        for label, values in self.runs.items():
            plt.plot(values, label=label)

        plt.legend()
        plt.xlabel("Episodio")
        plt.ylabel("Rendimiento")
        plt.title("Rendimiento política greedy")
        plt.grid(True)
        plt.savefig("graph_montecarlo.png")

