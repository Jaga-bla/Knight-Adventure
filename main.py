import pygame
import sys
from models import *

def main():
    #initialize screen
    pygame.init()
    clock = pygame.time.Clock()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    #initialize screen objects
    background = Background(0,0,screen,'mainmap.png',(1000,600))
    player = Player(800,300, screen, 'player.png', (50,100))
    merchant = Merchant(900,320, screen, 'merchant.png', (50,100))

    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                merchant.choose_option()

        if pygame.Rect.colliderect(player.rect, merchant.rect):
                merchant.menu_store(background)
        else:
            background = pygame.image.load('data/mainmap.png')

        if event.type == pygame.KEYDOWN:
            player.move(event)

        #display objects
        screen.blit(background, (0,0))
        merchant.blit_object()
        player.blit_object()
        pygame.display.flip()

if __name__ == '__main__':
    main()
