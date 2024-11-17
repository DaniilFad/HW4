
def lose_to_last_move_agent(observation, configuration):
    if observation.step > 0:
        return (observation.lastOpponentAction + 2) % configuration.signs
    else:
        return 0
