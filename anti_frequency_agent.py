
def anti_frequency_agent(observation, configuration):
    import numpy as np
    if observation.step == 0:
        anti_frequency_agent.counts = [0] * configuration.signs
    else:
        anti_frequency_agent.counts[observation.lastOpponentAction] += 1
    least_common = anti_frequency_agent.counts.index(min(anti_frequency_agent.counts))
    return (least_common + 1) % configuration.signs
