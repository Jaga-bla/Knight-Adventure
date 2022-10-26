import pygame
from .Enemy import Enemy

class Fight:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        image = pygame.image.load("data/fight_background.png")
        self.background = pygame.transform.scale(image, (1000, 600))
        self.enemy = Enemy(500,300, self.screen, 'enemy.png', (50,100))
        self.prize = True

    def init_enemy(self):
        self.enemy = Enemy(800,400,self.screen,'enemy.png',(50,100))

    def blit_objects(self):
        self.screen.blit(self.background,(0,0))
        self.player.blit_object()
        if self.enemy.is_alive:
            self.enemy.blit_object()

    def grant_prize(self):
        if self.enemy.is_alive() == False:
            if self.prize:
                self.player.lvl +=1
                self.player.wallet += random.randint(0,10)
                self.prize = False
    