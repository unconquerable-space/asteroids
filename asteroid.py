import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)

        velocities=[
            self.velocity.rotate(random_angle),
            self.velocity.rotate(-random_angle),
        ]

        for i in range(0, len(velocities)):
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocities[i] * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2) 
