import pygame
import random

from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity*dt

    def split(self) -> None:
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            split_angle = random.uniform(20, 50)
            new_vel_1 = self.velocity.rotate(split_angle)
            new_vel_2 = self.velocity.rotate(-split_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = new_vel_1*1.2
            asteroid_2.velocity = new_vel_2*1.2
