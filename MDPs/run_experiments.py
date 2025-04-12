from CorrectorMain import CorrectorMain



if __name__ == "__main__":
    experiment = CorrectorMain()
    experiment.run()
    initial_state_value = experiment.get_intial_value_state()
    print(experiment.get_execution_time())
    print(f"Valor de estado inicial: {initial_state_value}")
    experiment.get_optimal_policies_graph()