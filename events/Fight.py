import pygame
from models.Enemy import Enemy
import random

class Fight:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        image = pygame.image.load("data/fight_background.png")
        self.background = pygame.transform.scale(image, (1000, 600))
        self.enemy = Enemy(800,400,self.screen,'enemy.png',(50,100), self.player.lvl)
        self.prize = True

    def blit_objects(self):
        self.screen.blit(self.background,(0,0))
        self.player.blit_object()
        if self.enemy.is_alive:
            self.enemy.blit_object()

    def init_enemy(self):
        self.enemy = Enemy(800,400,self.screen,'enemy.png',(50,100), self.player.lvl)

    def grant_prize(self):
        if self.enemy.is_alive() == False:
            if self.prize:
                self.player.lvl +=1
                self.player.wallet += random.randint(2+self.player.lvl,10+self.player.lvl)
                self.prize = False

    def encounter(self, list_of_events):
        for event in list_of_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.attack(self.enemy)
        if self.player.is_alive() and self.enemy.is_alive():
            self.enemy.move(self.player)
        elif self.enemy.is_alive() == False:
            self.grant_prize()
            self.player.is_fighting = False
            return 
        if pygame.Rect.colliderect(self.player.rect, self.enemy.rect):
            self.enemy.attack(self.player)