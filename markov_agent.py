
import random

def markov_agent(observation, configuration):
    if observation.step == 0:
        markov_agent.prev_action = None
        markov_agent.transition_matrix = [[1/3]*3 for _ in range(3)]
        return random.randrange(0, configuration.signs)
    else:
        if markov_agent.prev_action is not None:
            last = markov_agent.prev_action
            curr = observation.lastOpponentAction
            markov_agent.transition_matrix[last][curr] += 1
            total = sum(markov_agent.transition_matrix[last])
            probs = [count / total for count in markov_agent.transition_matrix[last]]
            predicted = probs.index(max(probs))
            action = (predicted + 1) % configuration.signs
        else:
            action = random.randrange(0, configuration.signs)
        markov_agent.prev_action = observation.lastOpponentAction
        return action
