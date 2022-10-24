from .__models_interfaces import SurfaceObject

class Merchant(SurfaceObject):
    def create_menu(self):
        self.menu = MerchantShop(self.screen,'What can I do for you, Mighty Knight?')
