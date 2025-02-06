import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    
    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable,drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0

    #Create the game loop
    while True:
        #check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                print("Game Over!")
                sys.exit()
        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    s.kill()
                    a.split()

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
       
        
        pygame.display.flip()

        #limit framerate
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()