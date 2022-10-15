import pygame
from .models_interfaces import SurfaceObject

class Merchant(SurfaceObject):

    def menu_store(self, screen):
        menu = Menu(screen)
        self.option1 = menu.create_option(150, 'Buy sword')
        self.option2 = menu.create_option(220, 'Upgrade Sword')
        self.option3 = menu.create_option(290, 'Sell Sword')
        list_of_options = [self.option1, self.option2, self.option3]
        return list_of_options

    def choose_option(self, player):
        for option in self.menu_store(self.screen):
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                if option == self.option1:
                    player.gets_weapon()
                    player.init_weapon()
                    player.weapon.starting_power()
                if option == self.option2:
                    if player.has_weapon:
                        player.weapon.upgrade_weapon(5)
                        player.upgrade_weapon()
                    else:
                        print('you dont have weapon')
                if option == self.option3:
                    player.sells_weapon()
    
class Menu:
    def __init__(self, screen):
        self.screen = screen
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'Hello mighty Knight. What can i do for you?', True, (0,0,0))
        pygame.draw.rect(screen, (0,0,0), (50,50, 800,400))
        pygame.draw.rect(screen, (200,200,200), (70,70, 760,360))
        self.screen.blit(font,(300,120))

    def create_option(self, vertical_position:int, text:str):
        option = pygame.draw.rect(self.screen, (0,0,0), (300,vertical_position, 300,60))
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), text, True, (220,200,200))
        self.screen.blit(font,(400,vertical_position+20))
        return option