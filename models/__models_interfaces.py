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

class Character(SurfaceObject):
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        super().__init__(y, x, screen, name_of_image, size)
        self.lvl = 1

    def attack(self, target):
        target.health = target.health - self.power
    
    def move(self):
        pass

    def is_alive(self):
        if self.health >0:
            return True
        else:
            return False

class DrawMenu:
    def create_option(self, vertical_position:int, text:str):
        option = pygame.draw.rect(self.screen, (0,0,0), (300,vertical_position, 300,60))
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), text, True, (220,200,200))
        self.screen.blit(font,(400,vertical_position+20))
        return option

    def __init__(self, screen:pygame.Surface, heading:str):
        self.screen = screen
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), heading, True, (0,0,0))
        pygame.draw.rect(screen, (0,0,0), (50,50, 800,400))
        pygame.draw.rect(screen, (200,200,200), (70,70, 760,360))
        self.screen.blit(font,(300,120))

    def choose_option(self):
        pass
