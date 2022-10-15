import pygame
from .__models_interfaces import SurfaceObject, DrawMenu

class Background(SurfaceObject):
    pass
    def reload_screen(self, name_of_image):
        image = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image, self.size)

class InventoryView(DrawMenu):
    def __init__(self, screen:pygame.Surface, heading:str, player):
        self.screen = screen
        self.player = player
        font_heading = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), heading, True, (0,0,0))
        font_hp = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'HP: {player.health}/100', True, (0,0,0))
        font_off = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'Off: {player.offence}', True, (0,0,0))
        pygame.draw.rect(screen, (0,0,0), (1000,0, 300,600))
        pygame.draw.rect(screen, (200,200,200), (1020,20, 158,560))
        self.screen.blit(font_heading,(1060,20))
        self.screen.blit(font_hp,(1030,70))
        self.screen.blit(font_off,(1030,120))


