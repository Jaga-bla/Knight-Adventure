import pygame
from .models_interfaces import SurfaceObject

class Weapon(SurfaceObject):

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
    def attack_animation(self):
        pass