import pygame
import constants

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # ✅ Create the clock and delta time variable before the game loop
    clock = pygame.time.Clock()
    dt = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()

        # ✅ At the end of the loop: limit to 60 FPS, update dt
        dt = clock.tick(60) / 1000  # Convert ms to seconds

if __name__ == "__main__":
    main()
