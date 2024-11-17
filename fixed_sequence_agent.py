
def fixed_sequence_agent(observation, configuration):
    sequence = [0, 1, 2, 0, 2, 1]  # Предопределенная последовательность
    return sequence[observation.step % len(sequence)]
