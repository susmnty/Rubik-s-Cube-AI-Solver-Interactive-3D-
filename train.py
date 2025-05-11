from cube_env import CubeEnv
from dqn_agent import DQNAgent
import numpy as np
import torch

env = CubeEnv(scramble_steps=3)
state_size = 54
action_size = env.action_space()
    
agent = DQNAgent(state_size, action_size)
episodes = 1000
max_steps = 50

for ep in range(episodes):
    state = env.reset()
    total_reward = 0
    for t in range(max_steps):
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward
        if done:
            print(f"Episode {ep+1}: Solved in {t+1} moves, Total Reward: {total_reward:.2f}")
            break
    agent.replay()

    if (ep + 1) % 100 == 0:
        torch.save(agent.model.state_dict(), "model.pth")
        print(f"Model saved at episode {ep+1}")