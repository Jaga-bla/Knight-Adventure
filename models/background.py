import pygame
from .__models_interfaces import SurfaceObject

class Background(SurfaceObject):
    pass
    def reload_screen(self, name_of_image):
        image = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image, self.size)

class InventoryView:
    def __init__(self):
        pass