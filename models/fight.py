import pygame
from .enemy import Enemy
from .__models_interfaces import DrawMenu, SurfaceObject

class FightEntrance(SurfaceObject):
    def create_menu(self):
        self.menu = FightChoiceMenu(self.screen,'Are you ready for a fight?')

class FightChoiceMenu(DrawMenu):
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

        self.answer_yes = self.create_option(150, 'Yes')
        self.answer_no = self.create_option(220, 'No')
        self.list_of_options = [self.answer_yes, self.answer_no]


    def choose_option(self):
        for option in self.list_of_options:
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                if option == self.answer_yes:
                    pass
                if option == self.answer_no:
                    pass


class Fight:
    
    def __init__(self):
        image = pygame.image.load("data/fight_background.png")
        self.background = pygame.transform.scale(image, (1200, 600))

    def custom_initialization(self):
        self.enemy = Enemy(200,300, self.screen, 'player.png', (50,100))
        image = pygame.image.load("data/fight_background.png")
        self.background = pygame.transform.scale(image, (1200, 600))
        self.screen.blit(self.background, (0,0 ))
        self.player.blit_object()
        self.enemy.blit_object()