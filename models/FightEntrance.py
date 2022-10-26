from .__models_interfaces import SurfaceObject
from .FightChoiceMenu import FightChoiceMenu

class FightEntrance(SurfaceObject):
    def create_menu(self):
        self.menu = FightChoiceMenu(self.screen,'Are you ready for a fight?')