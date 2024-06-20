import numpy as np
import pygame

class Plane:
    def __init__(self):
        self.position = np.array([400.0, 300.0])
        self.velocity = np.array([0.0, 0.0])
        self.acceleration = np.array([0.0, 0.0])

    def update_position(self, keys):
        if keys[pygame.K_UP]:
            self.acceleration[1] -= 0.1
        if keys[pygame.K_DOWN]:
            self.acceleration[1] += 0.1
        if keys[pygame.K_LEFT]:
            self.acceleration[0] -= 0.1
        if keys[pygame.K_RIGHT]:
            self.acceleration[0] += 0.1

        self.velocity += self.acceleration
        self.position += self.velocity

        # Reset acceleration for the next frame
        self.acceleration = np.array([0.0, 0.0])
