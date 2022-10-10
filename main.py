import pygame
import sys
from models import *

pygame.init()
clock = pygame.time.Clock()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
background = pygame.image.load('data/mainmap.png')
player = Player('Knight')
keys = pygame.key.get_pressed()
moveLeft = False
moveRight = False
moveUp=False
moveDown =False
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        keys = pygame.key.get_pressed() 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moveRight = False
                moveLeft = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moveLeft = False
                moveRight = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                moveDown = False
                moveUp = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moveUp = False
                moveDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moveLeft = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moveRight = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                moveUp = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moveDown = False
        else:
            pass
    if moveDown and player.y < 500:
        player.y += 7
    if moveUp and player.y > 10:
        player.y -= 7
    if moveLeft and player.x > 10:
        player.x -= 7
    if moveRight and player.x < 900:
        player.x += 7
    screen.blit(background, (0,0))
    player.starting_position(screen)
    pygame.display.flip()
