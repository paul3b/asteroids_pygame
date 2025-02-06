import pygame # type: ignore
from constants import *

def main():
    print("Starting asteroids!")
    
    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Create the game loop
    while True:
        screen.fill((0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()