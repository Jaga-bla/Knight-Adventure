from .__models_interfaces import SurfaceObject
import pygame

class Enemy(SurfaceObject):
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 100
        self.offence = 1
        self.size = size
        image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))
        
    def move(self, player):
        Movement_speed = 3
        if player.y<self.y:
            self.y -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if player.y>self.y:
            self.y += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if player.y<self.y:
            self.x -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if player.x>self.x:
            self.x += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
            
    def attack(self, target):
        target.health = target.health - self.offence

    def is_alive(self):
        if self.health >0:
            return True
