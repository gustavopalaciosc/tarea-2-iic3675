from Algorithms.IterativePolicyEvaluation import IterativePolicyIteration
from Problems.GamblerProblem import GamblerProblem
from Problems.CookieProblem import CookieProblem
from Problems.GridProblem import GridProblem


if __name__ == "__main__":
    problem = GridProblem(grid_size=10)

    algorithm = IterativePolicyIteration(gamma=1.0, 
                                         problem=problem,
                                         threshold=0.0000000001)
    algorithm.run_uniform_policy()
    print(algorithm.get_initial_state_value())
