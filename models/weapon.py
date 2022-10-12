import pygame
from .models_interfaces import SurfaceObject

class Weapon(SurfaceObject):
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))

    def move(self, event):
        Movement_speed = 7
        if event.key == pygame.K_LEFT and self.y>10:
            self.y -= Movement_speed
        if event.key == pygame.K_RIGHT and self.y<950:
            self.y += Movement_speed
        if event.key == pygame.K_UP and self.x>10:
            self.x -= Movement_speed
        if event.key == pygame.K_DOWN and self.x<500:
            self.x += Movement_speed
    def starting_power(self):
        self.power = 5
        return self.power
    def upgrade_weapon(self, power_added):
        self.power = self.power + power_added