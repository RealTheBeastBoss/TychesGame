from meta import *
import random


class Dice:
    def __init__(self, sides, value_to_image):
        self.sides = sides
        self.sideFacing = sides
        self.valueToImage = value_to_image
        self.currentRect = None
        self.enabled = True


    def check_click(self, roll_dice = True):
        mouse_pos = pygame.mouse.get_pos()
        if Meta.LEFT_MOUSE_RELEASED and self.currentRect.collidepoint(mouse_pos) and self.enabled:
            self.enabled = False
            if roll_dice:
                if Meta.PLAYERS[Meta.CURRENT_PLAYER].setNextRoll is None or self.sides != 6:
                    self.sideFacing = random.randrange(1, self.sides + 1)
                else:
                    self.sideFacing = Meta.PLAYERS[Meta.CURRENT_PLAYER].setNextRoll
                    Meta.PLAYERS[Meta.CURRENT_PLAYER].setNextRoll = None
            return True
        return False
