import pygame
from .__models_interfaces import SurfaceObject,DrawMenu

class Merchant(SurfaceObject):
    def create_menu(self):
        self.menu = MerchantShop(self.screen,'Whant can I do for you, Mighty Knight?')
    
class MerchantShop(DrawMenu):
    def create_option(self, vertical_position:int, text:str):
        option = pygame.draw.rect(self.screen, (0,0,0), (300,vertical_position, 300,60))
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), text, True, (220,200,200))
        self.screen.blit(font,(400,vertical_position+20))
        return option

    def __init__(self, screen:pygame.Surface, heading:str):
        self.screen = screen
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), heading, True, (0,0,0))
        pygame.draw.rect(screen, (0,0,0), (50,50, 800,400))
        pygame.draw.rect(screen, (200,200,200), (70,70, 760,360))
        self.screen.blit(font,(300,120))

        self.option_buy = self.create_option(150, 'Buy Sword')
        self.option_upgrade = self.create_option(220, 'Upgrade Sword')
        self.option_sell = self.create_option(290, 'Sell Sword')

        self.list_of_options = [self.option_buy, self.option_upgrade, self.option_sell]

    def choose_option(self, player):
        for option in self.list_of_options:
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                if option == self.option_buy:
                    player.gets_weapon()
                    player.init_weapon()
                    player.weapon.starting_power()
                if option == self.option_upgrade:
                    if player.has_weapon:
                        player.weapon.upgrade_weapon(5)
                        player.upgrade_weapon()
                    else:
                        print('you dont have weapon')
                if option == self.option_sell:
                    player.sells_weapon()