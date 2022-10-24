import pygame
from .__models_interfaces import MovableObject
from .weapon import Weapon

class Player(MovableObject): 
    is_fighting = False
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.offence = 0
        self.wallet = 5
        self.health = 100
        self.lvl = 1
        image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))
        self.has_weapon = False

    def left_hand(self):
        position = (self.y-40, self.x -25)
        return position
    def right_hand(self):
        position = (self.y+40, self.x -25)
        return position

    def move(self, event):
        Movement_speed = 7
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
            target.health = target.health - (self.offence + self.weapon.power)

    def is_alive(self):
        if self.health >0:
            return True

    def gets_weapon(self):
        self.has_weapon = True

    def sells_weapon(self):
        self.has_weapon = False
        pygame.image.load('data/mainmap.png')
        self.offence = 0
        self.weapon.power = 0

    def init_weapon(self):
        position = self.right_hand()
        self.weapon = Weapon(position[0], position[1], self.screen, 'sword.png', (50,100))
        self.weapon.starting_power()
        self.offence = self.weapon.power

    def upgrade_weapon(self):
        self.offence = self.weapon.power
        print('weapon power', self.weapon.power)
        print('player offence', self.offence)

    def __str__(self):
        return self.name
