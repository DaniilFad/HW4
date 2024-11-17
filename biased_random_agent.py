
import random

def biased_random_agent(observation, configuration):
    choices = [0] * 50 + [1] * 25 + [2] * 25  # 50% камень, 25% бумага, 25% ножницы
    return random.choice(choices)
