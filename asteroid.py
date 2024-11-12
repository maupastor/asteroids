import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SCORE_BASE_VALUE

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0
        self.__kind = self.radius / ASTEROID_MIN_RADIUS
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_velocity_1 * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_velocity_2 * 1.2

    def get_score_value(self):
        return self.get_score_coefficient(self.__kind) * ASTEROID_SCORE_BASE_VALUE

    def get_score_coefficient(self, kind):
        if kind <= 1:
            return 1
        return self.triangle_number(kind) + self.get_score_coefficient(kind - 1)

    def triangle_number(self, n):
        return n * (n + 1) / 2