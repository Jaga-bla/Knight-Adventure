import pygame
from .__models_interfaces import SurfaceObject

class Weapon(SurfaceObject):
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        super().__init__(y, x, screen, name_of_image, size)
        self.image1 = pygame.image.load(f"data/sword.png")
        self.in_right_hand = True

    def move(self, event, list_of_events, player):
        Movement_speed = 7
        for event in list_of_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    position = player.weapon_position(-40)
                    self.y = position[0]
                    self.x = position[1]
                    self.in_right_hand = False
                if event.key == pygame.K_RIGHT:
                    position = player.weapon_position(40)
                    self.y = position[0]
                    self.x = position[1]
                    self.in_right_hand = True
        if event.key == pygame.K_LEFT and self.y>10:
            self.y -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_RIGHT and self.y<950:
            self.y += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_UP and self.x>10:
            self.x -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_DOWN and self.x<475:
            self.x += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
    def starting_power(self):
        self.power = 5
        return self.power
    def upgrade_weapon(self, power_added):
        self.power = self.power + power_added
    def attack_animation(self, event):
        image_attack = pygame.image.load("data/sword_attack.png")
        image_attack = pygame.transform.scale(image_attack, (100,50))
        image = pygame.transform.scale(self.image1, self.size)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.x = self.x + 50
                self.image = image_attack
                self.rect = self.image.get_rect(center= (self.y, self.x))
                if self.in_right_hand == False:
                    self.y =  self.y -50
                    self.image = pygame.transform.flip(image_attack, True, False)
                    self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.x = self.x - 50
                self.image = image
                self.rect = self.image.get_rect(center= (self.y, self.x))
                if self.in_right_hand == False:
                    self.y =  self.y +50
                    self.rect = self.image.get_rect(center= (self.y, self.x))
