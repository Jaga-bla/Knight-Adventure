import pygame
from .enemy import Enemy
from .merchant import Menu

class Fight:
    want_fight = False
    def menu_store(self, screen):
        self.screen = screen
        menu = Menu(screen)
        self.answer_yes = menu.create_option(150, 'Yes')
        self.answer_no = menu.create_option(220, 'No')
        list_of_options = [self.answer_yes, self.answer_no]
        return list_of_options

    def choose_option(self, player):
        self.player = player
        for option in self.menu_store(self.screen):
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                if option == self.answer_yes:
                    self.want_fight = True
                if option == self.answer_no:
                    pass
    
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