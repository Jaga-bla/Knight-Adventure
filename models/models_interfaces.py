import pygame

class SurfaceObject:
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))
        
    def blit_object(self):
        return self.screen.blit(self.image, (self.y, self.x))