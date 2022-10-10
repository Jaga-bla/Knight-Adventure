import pygame

class Weapon:
    def __init__(self) -> None:
        pass

class Armour:
    pass

class ChestPlate(Armour):
    pass

class Chausses(Armour):
    pass

class Shoes(Armour):
    pass

class Helmet(Armour):
    pass

class gloves(Armour):
    pass

class Player:
    def __init__(self, name:str):
        self.name = name
        self.health = 100
        self.defence = 0
        self.offence = 10
        self.x = 800
        self.y = 300
        image = pygame.image.load('data/player.png')
        self.image = pygame.transform.scale(image, (50,100))
        self.rect = self.image.get_rect()
    def starting_position(self, screen):
        return screen.blit(self.image, (self.x, self.y))
    def increase_off(self, value:int):
        self.offence = self.offence + value
        return self.offence
    def weapon(self):
        pass
    def increase_def(self, value:int):
        self.defence = self.defence + value
        return self.defence
    def attack(self):
        hit = self.offence
        return hit
    def __str__(self):
        return self.name
    def armour(self):
        pass

class Merchant:
    pass

class Enemy:
    pass