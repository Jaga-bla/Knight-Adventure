import pygame

class SurfaceObject:
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        pass
    def blit_object(self):
        return self.screen.blit(self.image, (self.y, self.x))