from CorrectorMain import CorrectorMain



if __name__ == "__main__":
    experiment = CorrectorMain()
    experiment.run()
    print(experiment.get_intial_value_state())
    print(experiment.get_execution_time())
    experiment.get_optimal_policies_graph()