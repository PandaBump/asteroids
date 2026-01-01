import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH #or SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    dt = 0 # Delta time between frames

    while True:
        log_state()

        for event in pygame.event.get(): # Event handling for quitting the game
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Player hit an asteroid!\nGame over!")
                sys.exit()
        pygame.display.flip()

        # Limit the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
