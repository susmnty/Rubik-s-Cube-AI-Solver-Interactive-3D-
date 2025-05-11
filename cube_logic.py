import numpy as np

class Cube:
    def __init__(self):
        self.faces = np.array([[i] * 9 for i in range(6)])  # 6 faces, each 3x3 (9)

    def rotate(self, move):
        if move == 'U':
            self.faces[0] = np.roll(self.faces[0], 1)
        elif move == 'U\'':
            self.faces[0] = np.roll(self.faces[0], -1)
        elif move == 'R':
            self.faces[1] = np.roll(self.faces[1], 1)
        elif move == 'R\'':
            self.faces[1] = np.roll(self.faces[1], -1)
        elif move == 'F':
            self.faces[2] = np.roll(self.faces[2], 1)
        elif move == 'F\'':
            self.faces[2] = np.roll(self.faces[2], -1)

    def is_solved(self):
        return all(np.all(face == face[0]) for face in self.faces)

    def to_array(self):
        return self.faces.copy()
    
    def __str__(self):
        return str(self.faces)
