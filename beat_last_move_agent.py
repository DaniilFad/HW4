
def beat_last_move_agent(observation, configuration):
    if observation.step > 0:
        return (observation.lastOpponentAction + 1) % configuration.signs
    else:
        return 0  # Начинает с "камня"
