import time
from Algorithms.IterativePolicyEvaluation import IterativePolicyEvaluation
from Algorithms.ValueIteration import ValueIteration
from Problems.GamblerProblem import GamblerProblem
from Problems.CookieProblem import CookieProblem
from Problems.GridProblem import GridProblem



"""
Recordar cambiar gamma según corresponde
"""

class CorrectorMain:
    def __init__(self):
        self.threshold = 0.0000000001
        self.problem = None
        self.gamma = None
        self.algorithm = None
        self.greedy = None
        self.exec_time = None

    
    def run(self):
        self.select_problem()

    def select_problem(self):
        while True:
            print("""
SELECCIÓN DE PROBLEMA
[1] Grid Problem
[2] Cookie Problem
[3] Gambler Problem""")
            option = input("Seleccione un problema: ")

            if option == "1":
                size = int(input("Ingrese el tamaño del grid: "))
                self.problem = GridProblem(grid_size=size)
                self.gamma = 1.0
                break
            elif option == "2":
                size = int(input("Ingrese el tamaño del grid: "))
                self.problem = CookieProblem(grid_size=size)
                self.gamma = 0.99
                break
            elif option == "3":
                p = float(input("Ingrese la probabilidad de cara: "))
                self.problem = GamblerProblem(prob_head=p)
                self.gamma = 1.0
                break
            else:
                print("Opción inválida.")
        self.select_algorithm()


    def select_algorithm(self):
        while True:
            print("""
SELECCIÓN DE ALGORITMO
[1] Iteratice Policy Evaluation
[2] Value Iteration
""")
            option = input("Seleccione algoritmo a evaluar: ")
            if option == "1":
                self.algorithm = IterativePolicyEvaluation(
                    gamma=self.gamma,
                    problem=self.problem,
                    threshold=self.threshold
                )
                self.select_policy()
                self.run_iterative_policy_evaluation()

                break
                
            elif option == "2":
                self.algorithm = ValueIteration(
                    gamma=self.gamma,
                    problem=self.problem,
                    threshold=self.threshold
                )
                self.run_value_iteration()
                break
            else:
                print("Opción inválida")
                pass



    def select_policy(self):
        while True:
            print("""
POLÍTICA A EJECUTAR
[1] Política Uniforme
[2] Política Greedy
""")
            option = input("Eliga la política que quiere probar: ")
            if option == "1":
                self.greedy = False
                break
            elif option == "2":
                self.greedy = True
                break
            else:
                print("Opción inválida")
                pass


    def get_optimal_policies_graph(self):
        if type(self.problem) == GamblerProblem:
            while True:

                print("""
¿Graficar políticas óptimas?
[1] Si
[2] No                  
""")            
                option = input("Ingrese opción: ")
                if option == "1":
                    filename = input("Ingrese nombre del gráfico: ")
                    self.algorithm.get_optimal_policies(filename=filename)
                    return
                elif option == "2":
                    break
                else:
                    print("Opción inválida")
                    pass
        return 
            

    def run_iterative_policy_evaluation(self):
        start = time.time()
        if self.greedy:
            self.algorithm.run_greedy_policy()
        else:
            self.algorithm.run_uniform_policy()
        end = time.time()
        self.exec_time = end - start
        return 
    

    def run_value_iteration(self):
        start = time.time()
        self.algorithm.run_value_iteration()
        end = time.time()
        self.exec_time = end - start
        return 

    def get_intial_value_state(self):
        return f"Valor del estado inicial: {self.algorithm.get_initial_state_value()}"


    def get_execution_time(self):
        return f"Tiempo de ejecución: {self.exec_time:.4f} segundos"

