import pygame
from .models_interfaces import SurfaceObject
from .weapon import Weapon

class Player(SurfaceObject): 
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.offence = 0
        image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))
        self.has_weapon = False

    def move(self, event):
        Movement_speed = 7
        if event.key == pygame.K_LEFT and self.y>-80:
            self.y -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_RIGHT and self.y<990:
            self.y += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_UP and self.x>10:
            self.x -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_DOWN and self.x<500:
            self.x += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))

    def gets_weapon(self):
        self.has_weapon = True

    def sells_weapon(self):
        self.has_weapon = False
        pygame.image.load('data/mainmap.png')
        self.offence = 0
        self.weapon.power = 0

    def init_weapon(self):
        self.weapon = Weapon(self.y+40, self.x-25, self.screen, 'sword.png', (50,100))
        self.weapon.starting_power()
        self.offence = self.offence + self.weapon.power

    def upgrade_weapon(self):
        self.offence = self.weapon.power
        print('weapon power', self.weapon.power)
        print('player offence', self.offence)


    def draw_rect(self):
        pygame.draw.rect(self.rect)

    def __str__(self):
        return self.name