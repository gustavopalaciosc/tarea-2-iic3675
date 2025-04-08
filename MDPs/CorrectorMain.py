from Algorithms.IterativePolicyEvaluation import IterativePolicyIteration
from Problems.GamblerProblem import GamblerProblem
from Problems.CookieProblem import CookieProblem
from Problems.GridProblem import GridProblem


"""
Recordar cambiar gamma según corresponde
"""


if __name__ == "__main__":
    #problem = GridProblem(grid_size=10)
    #problem = CookieProblem(grid_size=10)
    problem = GamblerProblem(prob_head=0.55)

    algorithm = IterativePolicyIteration(gamma=1.0, 
                                         problem=problem,
                                         threshold=0.0000000001)
    algorithm.run_greedy_policy()
    #algorithm.run_uniform_policy()
    print(algorithm.get_initial_state_value())

