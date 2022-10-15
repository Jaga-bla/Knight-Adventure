from models.enemy import Enemy
from models.fight import Fight

def encounter(fight):

    fight.blit_objects()
    fight.enemy.move(fight.player)