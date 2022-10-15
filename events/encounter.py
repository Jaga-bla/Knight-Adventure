import pygame

def encounter(fight, event, list_of_events):
    for event in list_of_events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fight.player.attack(fight.enemy)
    if fight.enemy.is_alive():
        fight.blit_objects()
    if fight.player.is_alive() and fight.enemy.is_alive():
        fight.enemy.move(fight.player)
    if pygame.Rect.colliderect(fight.player.rect, fight.enemy.rect):
        fight.enemy.attack(fight.player)