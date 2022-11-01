
import pygame 
from .__models_interfaces import DrawMenu

class FightChoiceMenu(DrawMenu):

    def __init__(self, screen:pygame.Surface, heading:str):
        super().__init__(screen, heading)

        self.answer_yes = self.create_option(150, 'Yes')
        self.answer_no = self.create_option(220, 'No')
        self.list_of_options = [self.answer_yes, self.answer_no]


    def choose_option(self):
        for option in self.list_of_options:
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                if option == self.answer_yes:
                    return True
                if option == self.answer_no:
                    return False
