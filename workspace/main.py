# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
    pygame.init()
    # Welcome message + screen size
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # Create the screen for the player
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # Game Loop
    while True:
        # This will kill the game if the user closes the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen with black space
        screen.fill((0,0,0))
        # Refresh the sceen
        pygame.display.flip()

if __name__ == "__main__":
    main()