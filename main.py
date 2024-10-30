import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids,updateable,drawable)

    AsteroidField.containers = (updateable)
    asteroidfield = AsteroidField()

    Shot.containers = (shots,updateable,drawable)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        for item in updateable:
            item.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit("Game over!")
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
