from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    containers = []  # This allows it to be added to sprite groups

    def __init__(self, position, velocity):
        # Unpack Vector2 position into x and y
        super().__init__(position.x, position.y, constants.SHOT_RADIUS)
        self.velocity = velocity
        # Add this shot to the groups (if set)
        if hasattr(self, 'add'):
            self.add(*self.containers)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), constants.SHOT_RADIUS)
