import sys
from models.Background import *
from models.Merchant import *
from models.Player import *
from events.Fight import *
from models.FightEntrance import *


class GameDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(0,0,screen,'mainmap.png',(1000,600))
        self.player = Player(800,300, screen, 'player.png', (50,100))
        self.merchant = Merchant(900,400, screen, 'merchant.png', (50,100))
        self.fight_entrance = FightEntrance(0,0, screen, 'cave.png', (200,200))
        self.inventory = InventoryView(screen, 'Inventory', self.player)
        self.fight = Fight(self.player, screen)

    def main_map(self):
        self.inventory.blit_menu()
        self.background.blit_object()
        self.merchant.blit_object()
        self.fight_entrance.blit_object()
        self.player.blit_object()
        if self.player.has_weapon == True:
            self.player.weapon.blit_object()

        if pygame.Rect.colliderect(self.player.rect, self.merchant.rect):
            self.merchant.create_menu()

        if pygame.Rect.colliderect(self.player.rect, self.fight_entrance.rect):
            self.fight_entrance.create_menu()

    def fight_map(self):
        self.inventory.blit_menu()
        self.fight.blit_objects()
        if self.player.has_weapon == True:
            self.player.weapon.blit_object()

    def run_game(self, event, list_of_events):
        if self.player.is_alive() == False:
            sys.exit()
        self.player.move(event)
        if self.player.has_weapon:
            self.player.weapon.move(event, self.player)
            self.player.weapon.attack_animation(list_of_events)
        if self.player.is_fighting == False:
            self.main_map()
            for event in list_of_events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.colliderect(self.player.rect, self.merchant.rect):
                        self.merchant.menu.choose_option(self.player)
                    if pygame.Rect.colliderect(self.player.rect, self.fight_entrance.rect):
                        self.player.is_fighting = self.fight_entrance.menu.choose_option()
                        self.fight = Fight(self.player, self.screen)               
        if self.player.is_fighting == True:
            self.fight.encounter(list_of_events)
            self.fight_map()