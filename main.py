import pygame
import sys
from events.GameDisplay import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    size = width, height = 1200, 600
    screen = pygame.display.set_mode(size)
    game_display = GameDisplay(screen)

    while 1:
        clock.tick(60)
        list_of_events = pygame.event.get() 

        for event in list_of_events:
            if event.type == pygame.QUIT:
                sys.exit()  

        game_display.run_game(event, list_of_events)               

        pygame.display.flip()

if __name__ == '__main__':
    main() 