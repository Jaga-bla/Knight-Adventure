import pygame

class Object:
    #an object at screen surface, created with png image and (x,y) position
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
    def get_position(self):
        return [self.y, self.x]
    def draw_rect(self):
        pygame.draw.rect(self.rect)

class Weapon(Object):
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

class Background(Object):
    pass

class Player(Object): 
    def __init__(self, y : int, x :int, screen:pygame.Surface, name_of_image: str, size : tuple):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        image1 = pygame.image.load(f"data/{name_of_image}")
        self.image = pygame.transform.scale(image1, self.size)
        self.rect = self.image.get_rect(center= (self.y, self.x))
        self.has_weapon = False

    def move(self, event):
        Movement_speed = 7

        if event.key == pygame.K_LEFT and self.y>10:
            self.y -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_RIGHT and self.y<950:
            self.y += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_UP and self.x>10:
            self.x -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if event.key == pygame.K_DOWN and self.x<500:
            self.x += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))

    def increase_off(self, value:int):
        self.offence = self.offence + value
        return self.offence

    def gets_weapon(self):
        self.has_weapon = True

    def init_sword(self):
        self.weapon = Weapon(self.y+50, self.x, self.screen, 'sword.png', (50,100))

    def __str__(self):
        return self.name


class Merchant(Object):
    def menu_store(self, background):
        self.background = background
        menu = Menu(self.background )
        self.option1 = menu.option(150, 'Buy sword')
        self.option2 = menu.option(220, 'Upgrade Sword')
        self.option3 = menu.option(290, 'Sell Sword')
        list_of_options = [self.option1, self.option2, self.option3]
        return list_of_options
    def choose_option(self, player):
        for option in self.menu_store(self.background):
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                player.gets_weapon()
                player.init_sword()


class Menu(Object):
    def __init__(self, background):
        self.background = background
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), f'Hello mighty Knight. What can i do for you?', True, (0,0,0))
        pygame.draw.rect(background, (0,0,0), (50,50, 800,400))
        pygame.draw.rect(background, (200,200,200), (70,70, 760,360))
        self.background.blit(font,(300,120))
    def option(self, vertical_position:int, text:str):
        option = pygame.draw.rect(self.background, (0,0,0), (300,vertical_position, 300,60))
        font = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 24), text, True, (220,200,200))
        self.background.blit(font,(400,vertical_position+20))
        return option
    

class Enemy:
    pass