from Problems.GridProblem import GridProblem
from Problems.CookieProblem import CookieProblem
from Problems.GamblerProblem import GamblerProblem
from Algorithms.ValueIteration import ValueIteration


if __name__ == "__main__":
    #problem = CookieProblem(grid_size=3)
    problem = GamblerProblem(prob_head=0.55)
    #problem = GridProblem(grid_size=10)
    

    # RECORDAR CAMBIAR GAMMA SEGÚN EL PROBLEMA
    algoritmo = ValueIteration(gamma=1.0, problem=problem)
    algoritmo.run_value_iteration()
    print(algoritmo.get_initial_state_value())