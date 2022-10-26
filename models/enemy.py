from .__models_interfaces import MovableObject
import pygame

class Enemy(MovableObject):

    def is_alive(self):
        if self.health >0:
            return True
        else:
            return False

    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        super().__init__(y, x, screen, name_of_image, size)
        self.health = 100
        self.offence = 1
        self.is_alive()
        
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
        
