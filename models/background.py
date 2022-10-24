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
        self.font_heading = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), heading, True, (0,0,0))
        self.font_hp = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'HP: {player.health}/100', True, (0,0,0))
        self.font_off = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'Off: {player.offence}', True, (0,0,0))
        self.font_wallet = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'Wallet: {player.wallet} berries', True, (0,0,0))
        self.font_lvl = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'Lvl: {player.lvl}', True, (0,0,0))

    def blit_menu(self):
        pygame.draw.rect(self.screen, (0,0,0), (1000,0, 300,600))
        pygame.draw.rect(self.screen, (200,200,200), (1020,20, 158,560))
        self.screen.blit(self.font_heading,(1060,20))
        self.screen.blit(self.font_hp,(1030,70))
        self.screen.blit(self.font_off,(1030,120))
        self.screen.blit(self.font_wallet,(1030,170))
        self.screen.blit(self.font_lvl,(1030,270))



