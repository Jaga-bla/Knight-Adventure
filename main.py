import pygame
import sys
from models.background import *
from models.merchant import *
from models.player import *
from models.fight import *
from events.encounter import encounter


def main():
    #initialize screen
    pygame.init()
    clock = pygame.time.Clock()
    size = width, height = 1200, 600
    screen = pygame.display.set_mode(size)

    #initialize screen objects
    background = Background(0,0,screen,'mainmap.png',(1000,600))
    player = Player(800,300, screen, 'player.png', (50,100))
    merchant = Merchant(900,400, screen, 'merchant.png', (50,100))
    fight_entrance = FightEntrance(0,0, screen, 'cave.png', (200,200))
    ready_to_fight = False

    while 1:
        inventory = InventoryView(screen, 'Inventory', player)
        background.blit_object()
        merchant.blit_object()
        fight_entrance.blit_object()
        player.blit_object()
        clock.tick(60)
        list_of_events = pygame.event.get()

        for event in list_of_events:
            if event.type == pygame.QUIT:
                sys.exit()
            if player.has_weapon:
                player.weapon.attack_animation(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.colliderect(player.rect, merchant.rect) and player.is_fighting == False:
                    merchant.menu.choose_option(player)
                if pygame.Rect.colliderect(player.rect, fight_entrance.rect) and player.is_fighting == False:
                    ready_to_fight = fight_entrance.menu.choose_option()
                    fight = Fight(player, screen)

        if ready_to_fight == True:
            player.is_fighting = True
            encounter(fight, event, list_of_events)

        if player.has_weapon == True:
            player.weapon.blit_object()
        
        if pygame.Rect.colliderect(player.rect, merchant.rect) and player.is_fighting == False:
            merchant.create_menu()

        if pygame.Rect.colliderect(player.rect, fight_entrance.rect) and player.is_fighting == False:
            fight_entrance.create_menu()

        if event.type == pygame.KEYDOWN:
            player.move(event)
            if player.has_weapon:
                player.weapon.move(event, list_of_events, player)

        pygame.display.flip()

if __name__ == '__main__':
    main() 