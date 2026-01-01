import pygame
from constants import * #or SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create a clock object to manage frame rate
    dt = 0 # Delta time between frames

    while 1 > 0:
        log_state()

        for event in pygame.event.get(): # Event handling for quitting the game
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
