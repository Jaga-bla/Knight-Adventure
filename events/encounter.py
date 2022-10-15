from models.enemy import Enemy
from models.fight import Fight

def encounter(player, screen, event):
    enemy = Enemy(800,400,screen,'enemy.png',(50,100)
    )
    fight = Fight(player, screen, enemy)