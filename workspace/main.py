import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    shots = []

    # Sprite groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    # Assign static containers
    Player.containers = [updatables, drawables]
    Asteroid.containers = [updatables, drawables, asteroids]
    AsteroidField.containers = [updatables]
    Shot.containers = [updatables, drawables, shots] 

    # Instantiate objects
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid = Asteroid(100, 100, 40)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player.shoot()
        
        for obj in updatables:
            obj.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print ("Game over!")
                return
        
        screen.fill((0, 0, 0))
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
