import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Time-related information
    clock = pygame.time.Clock()
    dt = 0.0
    
    # Screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups of Objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers=(updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Object Instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    #Initiate Game Loop
    while True:
        log_state()

        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        for object in updatable:
            object.update(dt)

        for object in drawable:
            object.draw(screen)
        
        # Update Everything to Screen
        pygame.display.flip()

        # Check for Player-Asteroid Collision
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit() 
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

if __name__ == "__main__":
    main()
