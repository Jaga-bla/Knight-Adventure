import pygame
from .__models_interfaces import SurfaceObject

class Weapon(SurfaceObject):
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(self.image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))

    def move(self, event, list_of_events, player):
        Movement_speed = 7
        for event in list_of_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    position = player.left_hand()
                    self.y = position[0]
                    self.x = position[1]
                if event.key == pygame.K_RIGHT:
                    position = player.right_hand()
                    self.y = position[0]
                    self.x = position[1]
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
        if event.key == pygame.K_SPACE:
            self.image = image_attack
            self.screen.blit(self.image,(self.y+50, self.x))
        else:
            self.image = pygame.transform.scale(self.image1, self.size)