from cube_logic import Cube
import numpy as np
import random

class CubeEnv:
    def __init__(self, scramble_steps=3):
        self.scramble_steps = scramble_steps
        self.num_actions = 6  # Let's say 6 moves: U, U', R, R', F, F'
        self.moves = ['U', "U'", 'R', "R'", 'F', "F'"]
        self.cube = Cube()

    def reset(self):
        self.cube = Cube()
        for _ in range(self.scramble_steps):
            move = random.choice(self.moves)
            self.cube.rotate(move)
        return self._get_state()

    def step(self, action):
        move = self.moves[action]
        self.cube.rotate(move)
        state = self._get_state()
        reward = 1.0 if self.cube.is_solved() else -0.1
        done = self.cube.is_solved()
        return state, reward, done

    def _get_state(self):
        return self.cube.to_array().flatten()

    def action_space(self):
        return self.num_actions