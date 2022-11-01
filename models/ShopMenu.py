import pygame
from .__models_interfaces import DrawMenu

class ShopMenu(DrawMenu):

    def __init__(self, screen:pygame.Surface, heading:str):
        super().__init__(screen, heading)

        self.option_buy = self.create_option(150, f'Buy Sword    5 berries')
        self.option_upgrade = self.create_option(220, 'Upgrade Sword    5 berries')
        self.option_sell = self.create_option(290, 'Sell Sword   +5 berries')

        self.list_of_options = [self.option_buy, self.option_upgrade, self.option_sell]

    def choose_option(self, player):
        for option in self.list_of_options:
            if pygame.Rect.collidepoint(option, pygame.mouse.get_pos()):
                if option == self.option_buy and player.has_weapon == False:
                    player.wallet -=5
                    print(player.wallet)
                    player.init_weapon()
                    player.weapon.starting_power()
                    player.weapon.blit_object()
                if option == self.option_upgrade:
                    if player.wallet >=5:
                        if player.has_weapon:
                            player.wallet -=5
                            player.weapon.upgrade_weapon(5)
                            player.change_power()
                        else:
                            self.__init__(self.screen, "You don't have a weapon")
                    else:
                        print('you dont have enough berries')
                if option == self.option_sell:
                    if player.has_weapon:
                        player.wallet +=5
                        player.sells_weapon()
                    else:
                        print('you dont have weapon')