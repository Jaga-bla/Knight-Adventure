
import pygame 
from .__models_interfaces import DrawMenu

class FightChoiceMenu(DrawMenu):
    def create_option(self, vertical_position:int, text:str):
        option = pygame.draw.rect(self.screen, (0,0,0), (300,vertical_position, 300,60))
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), text, True, (220,200,200))
        self.screen.blit(font,(400,vertical_position+20))
        return option

    def __init__(self, screen:pygame.Surface, heading:str):
        self.screen = screen
        self.heading = heading
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), self.heading, True, (0,0,0))
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
                    ready_to_fight = True
                    return ready_to_fight
                if option == self.answer_no:
                    ready_to_fight = False
                    return ready_to_fight
