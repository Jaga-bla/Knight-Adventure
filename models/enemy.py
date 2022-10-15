from .__models_interfaces import SurfaceObject

class Enemy(SurfaceObject):
    def move(self, player):
        Movement_speed = 3
        if player.y<self.y:
            self.y -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if player.y>self.y:
            self.y += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if player.y<self.y:
            self.x -= Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
        if player.x>self.x:
            self.x += Movement_speed
            self.rect = self.image.get_rect(center= (self.y, self.x))
