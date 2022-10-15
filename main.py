import pygame
import sys
from models.background import *
from models.merchant import *
from models.player import *
from models.fight import *
from events import encounter


def main():
    #initialize screen
    pygame.init()
    clock = pygame.time.Clock()
    size = width, height = 1200, 600
    screen = pygame.display.set_mode(size)

    #initialize screen objects
    background = Background(0,0,screen,'mainmap.png',(1000,600))
    player = Player(800,300, screen, 'player.png', (50,100))
    merchant = Merchant(900,320, screen, 'merchant.png', (50,100))
    fight_entrance = FightEntrance(0,0, screen, 'cave.png', (200,200))
    ready_to_fight = False

    while 1:
        background.blit_object()
        merchant.blit_object()
        fight_entrance.blit_object()
        player.blit_object()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.colliderect(player.rect, merchant.rect):
                    merchant.menu.choose_option(player)
                if pygame.Rect.colliderect(player.rect, fight_entrance.rect):
                    ready_to_fight = fight_entrance.menu.choose_option()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("y")

        if pygame.Rect.colliderect(player.rect, merchant.rect):
            merchant.create_menu()


        if pygame.Rect.colliderect(player.rect, fight_entrance.rect):
            fight_entrance.create_menu()

        if ready_to_fight == True:
            encounter(player, screen, event)

        if event.type == pygame.KEYDOWN:
            player.move(event)
            if player.has_weapon:
                player.weapon.move(event)
        if player.has_weapon == True:
            player.weapon.blit_object()
        pygame.display.flip()

if __name__ == '__main__':
    main()