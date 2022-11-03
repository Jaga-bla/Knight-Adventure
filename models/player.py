import pygame
from .__models_interfaces import Character
from .Weapon import Weapon

class Player(Character): 

    is_fighting = False

    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        super().__init__(y, x, screen, name_of_image, size)
        self.power = 0
        self.wallet = 5
        self.health = 100
        self.has_weapon = False

    def weapon_position(self, vertical_position:int):
        position = (self.y+vertical_position, self.x -25)
        return position

    def move(self, event):
        Movement_speed = 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.y>0:
                self.y -= Movement_speed
                self.rect = self.image.get_rect(center= (self.y, self.x))
            if event.key == pygame.K_RIGHT and self.y<940:
                self.y += Movement_speed
                self.rect = self.image.get_rect(center= (self.y, self.x))
            if event.key == pygame.K_UP and self.x>10:
                self.x -= Movement_speed
                self.rect = self.image.get_rect(center= (self.y, self.x))
            if event.key == pygame.K_DOWN and self.x<500:
                self.x += Movement_speed
                self.rect = self.image.get_rect(center= (self.y, self.x))

    def attack(self, target):
        if pygame.Rect.colliderect(self.weapon.rect, target.rect):
            target.health = target.health - (self.power + self.weapon.power)

    def sells_weapon(self):
        self.has_weapon = False
        self.power = 0
        self.weapon.power = 0

    def init_weapon(self):
        self.has_weapon = True
        position = self.weapon_position(40)
        self.weapon = Weapon(position[0], position[1], self.screen, 'sword.png', (50,100))
        self.weapon.starting_power()
        self.power = self.weapon.power

    def change_power(self):
        self.power = self.weapon.power
