import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.velocity = pygame.Vector2(0, 1)
        self.split_angle = random.uniform(20, 50)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_velocity1 = self.velocity.rotate(self.split_angle)
        new_velocity2 = self.velocity.rotate(-self.split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * SPLIT_VELOCITY_MULTIPLIER
        new_asteroid2.velocity = new_velocity2 * SPLIT_VELOCITY_MULTIPLIER
