import pygame
from .models import SurfaceObject

class Merchant(SurfaceObject):
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))

    def menu_store(self, background):
        self.background = background
        menu = Menu(self.background )
        self.option1 = menu.create_option(150, 'Buy sword')
        self.option2 = menu.create_option(220, 'Upgrade Sword')
        self.option3 = menu.create_option(290, 'Sell Sword')
        list_of_options = [self.option1, self.option2, self.option3]
        return list_of_options

    def choose_option(self, player):
        for option in self.menu_store(self.background):
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                if option == self.option1:
                    player.gets_weapon()
                    player.init_weapon()
                    player.weapon.starting_power()
                if option == self.option2:
                    player.weapon.upgrade_weapon(5)
                    player.upgrade_weapon()
                    print('weapon power',player.weapon.power)
                    print('player offence',player.offence)
                if option == self.option3:
                    player.sells_weapon()
                    
    def draw_rect(self):
        pygame.draw.rect(self.rect)

class Menu:
    def __init__(self, background):
        self.background = background
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'Hello mighty Knight. What can i do for you?', True, (0,0,0))
        pygame.draw.rect(background, (0,0,0), (50,50, 800,400))
        pygame.draw.rect(background, (200,200,200), (70,70, 760,360))
        self.background.blit(font,(300,120))

    def create_option(self, vertical_position:int, text:str):
        option = pygame.draw.rect(self.background, (0,0,0), (300,vertical_position, 300,60))
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), text, True, (220,200,200))
        self.background.blit(font,(400,vertical_position+20))
        return option
    

