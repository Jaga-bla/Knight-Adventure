
import pygame 
from .__models_interfaces import DrawMenu

class FightEntryMenu(DrawMenu):
    def __init__(self, screen:pygame.Surface, heading:str):
        self.screen = screen
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), heading, True, (0,0,0))
        pygame.draw.rect(screen, (0,0,0), (50,50, 800,400))
        pygame.draw.rect(screen, (200,200,200), (70,70, 760,360))
        self.screen.blit(font,(300,120))

        self.option1 = self.create_option(self, 250, 'Option1 text')

        self.list_of_options = [self.option1]

    def choose_option(self):
        for option in self.list_of_options:
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                pass