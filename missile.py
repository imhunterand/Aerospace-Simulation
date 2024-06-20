import numpy as np

class Missile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.target = None
        self.speed = 5

    def set_target(self, target):
        self.target = target

    def update_position(self):
        if self.target is not None:
            direction = self.target - self.position
            distance = np.linalg.norm(direction)
            if distance > 0:
                direction /= distance
            self.velocity = direction * self.speed
        self.position += self.velocity
