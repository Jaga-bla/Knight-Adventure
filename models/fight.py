import pygame
from .Enemy import Enemy
import random

class Fight:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        image = pygame.image.load("data/fight_background.png")
        self.background = pygame.transform.scale(image, (1000, 600))
        self.enemy = Enemy(800,400,self.screen,'enemy.png',(50,100))
        self.prize = True

    def blit_objects(self):
        self.screen.blit(self.background,(0,0))
        self.player.blit_object()
        if self.enemy.is_alive:
            self.enemy.blit_object()

    def grant_prize(self):
        if self.enemy.is_alive() == False:
            if self.prize:
                self.player.lvl +=1
                self.player.wallet += random.randint(2,10)
                self.prize = False

    def proceed(self, list_of_events):
        self.enemy.move(self.player)
        for event in list_of_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.attack(self.enemy)
        if self.enemy.is_alive() == False:
            self.grant_prize()
        if pygame.Rect.colliderect(self.player.rect, self.enemy.rect):
            self.enemy.attack(self.player)
        self.blit_objects()