
def frequency_agent(observation, configuration):
    import numpy as np
    if observation.step == 0:
        frequency_agent.counts = [0] * configuration.signs
    else:
        frequency_agent.counts[observation.lastOpponentAction] += 1
    most_common = frequency_agent.counts.index(max(frequency_agent.counts))
    return (most_common + 1) % configuration.signs
