from circleshape import CircleShape
from shot import Shot
import constants
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, direction, dt):
        self.rotation += direction * constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = direction * constants.PLAYER_SHOOT_SPEED
        return Shot(self.position.copy(), velocity)
