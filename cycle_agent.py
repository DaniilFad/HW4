
def cycle_agent(observation, configuration):
    return observation.step % configuration.signs
