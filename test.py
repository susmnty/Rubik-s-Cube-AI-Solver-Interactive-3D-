from cube_env import CubeEnv
from dqn_agent import QNetwork
import torch

env = CubeEnv(scramble_steps=3)
model = QNetwork(54, env.action_space())
model.load_state_dict(torch.load("model.pth"))
model.eval()

state = env.reset()
done = False
steps = 0

while not done and steps < 50:
    state_tensor = torch.FloatTensor(state).unsqueeze(0)
    with torch.no_grad():
        action = torch.argmax(model(state_tensor)).item()
    state, reward, done = env.step(action)
    steps += 1

print(f"Solved in {steps} steps" if done else "Failed to solve")