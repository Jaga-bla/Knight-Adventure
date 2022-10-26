from .__models_interfaces import SurfaceObject
from .ShopMenu import ShopMenu

class Merchant(SurfaceObject):
    def create_menu(self):
        self.menu = ShopMenu(self.screen,'What can I do for you, Mighty Knight?')
