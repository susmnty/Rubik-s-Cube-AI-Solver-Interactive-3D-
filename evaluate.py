# evaluate.py
from cube_env import CubeEnv
from dqn_agent import QNetwork
import torch

# Set up the environment and model
env = CubeEnv(scramble_steps=3)
model = QNetwork(54, env.action_space())
model.load_state_dict(torch.load("model.pth"))
model.eval()

# Initialize the environment and variables
state = env.reset()
done = False
steps = 0

# Run the agent through the environment to test
while not done and steps < 50:
    state_tensor = torch.FloatTensor(state).unsqueeze(0)  # Convert state to tensor
    with torch.no_grad():
        action = torch.argmax(model(state_tensor)).item()  # Get action from model
    state, reward, done = env.step(action)  # Take the action in the environment
    steps += 1

# Output the results
print(f"Solved in {steps} steps" if done else "Failed to solve")

# Add this at the top
solved_moves = []

# In your loop
while not done and steps < 50:
    state_tensor = torch.FloatTensor(state).unsqueeze(0)
    with torch.no_grad():
        action = torch.argmax(model(state_tensor)).item()
    state, reward, done = env.step(action)
    steps += 1
    solved_moves.append(env.moves[action])  # track the move

# Save to file
with open("moves.txt", "w") as f:
    f.write(",".join(solved_moves))