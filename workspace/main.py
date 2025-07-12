import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField  # <-- Make sure to import it

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Sprite groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Assign static containers
    Player.containers = [updatables, drawables]
    Asteroid.containers = [updatables, drawables, asteroids]
    AsteroidField.containers = [updatables]  # <-- only updatables

    # Instantiate objects
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid = Asteroid(100, 100, 40)
    asteroid_field = AsteroidField()  # <-- This completes step 2

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
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
