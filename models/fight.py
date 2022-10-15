import pygame
from .enemy import Enemy

class Fight:
    def __init__(self, player, screen):
        self.player = player
        self.enemy = Enemy(200,300, screen, 'player.png', (50,100))
        image = pygame.image.load("data/fight_background.png")
        self.background = pygame.transform.scale(image, (1200, 600))
        screen.blit(self.background, (0,0 ))
        self.player.blit_object()
        self.enemy.blit_object()