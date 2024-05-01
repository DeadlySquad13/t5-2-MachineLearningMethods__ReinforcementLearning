import sys

import gym

from toy_environment.consts import CLIFF_WALKING_ENV

from time_difference_algorithms.basic_agent import BasicAgent
from time_difference_algorithms.sarsa_agent import SarsaAgent
from time_difference_algorithms.q_learning_agent import QLearningAgent
from time_difference_algorithms.double_q_learning_agent import DoubleQLearningAgent

ENV = CLIFF_WALKING_ENV


def play_agent(agent):
    """
    Проигрывание сессии для обученного агента
    """
    env = gym.make(ENV["name"], render_mode="human")
    state = env.reset()[0]
    done = False
    while not done:
        action = agent.greedy(state)
        next_state, reward, terminated, truncated, _ = env.step(action)
        env.render()
        state = next_state
        if terminated or truncated:
            done = True


def run_algorithm(agent: BasicAgent):
    agent.learn()
    agent.print_q()
    agent.draw_episodes_reward()
    play_agent(agent)


def run_sarsa():
    env = gym.make(ENV["name"])
    agent = SarsaAgent(env)

    run_algorithm(agent)


def run_q_learning():
    env = gym.make(ENV["name"])
    agent = QLearningAgent(env)

    run_algorithm(agent)


def run_double_q_learning():
    env = gym.make(ENV["name"])
    agent = DoubleQLearningAgent(env)

    run_algorithm(agent)


def main(algorithm: str):
    match algorithm:
        case "sarsa":
            run_sarsa()
        case "q_learning":
            run_q_learning()
        case "double_q_learning":
            run_double_q_learning()
        case _:
            print("Choose algorithm from one of the existing")


if __name__ == "__main__":
    print(sys.argv)

    if len(sys.argv) < 2:
        raise Exception('Please choose algorithm by passing argument')

    main(algorithm=sys.argv[1])
