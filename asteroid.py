from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_state, log_event
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle: float = random.uniform(20, 50)
        first_velocity_vector = self.velocity.rotate(random_angle)
        second_velocity_vector = self.velocity.rotate(random_angle * -1)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        first_new_asteroid.velocity = first_velocity_vector * 1.2
        second_new_asteroid.velocity = second_velocity_vector * 1.2

