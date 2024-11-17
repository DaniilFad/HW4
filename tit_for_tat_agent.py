
def tit_for_tat_agent(observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return 0  # Начинает с "камня"
