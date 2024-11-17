
import random

def mirror_agent(observation, configuration):
    global my_last_action
    if observation.step == 0:
        # На первом шаге выбираем случайное действие и сохраняем его
        action = random.randrange(0, configuration.signs)
        my_last_action = action
    else:
        # Выбираем действие, которое побеждает наше предыдущее действие
        action = (my_last_action + 1) % configuration.signs
        # Обновляем наше последнее действие для следующего хода
        my_last_action = action
    return action

