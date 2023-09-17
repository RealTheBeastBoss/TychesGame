from meta import *
import random


class Dice:
    def __init__(self, sides, value_to_image):
        self.sides = sides
        self.sideFacing = sides
        self.valueToImage = value_to_image
        self.currentRect = None
        self.enabled = False


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if Meta.LEFT_MOUSE_RELEASED and self.currentRect.collidepoint(mouse_pos) and self.enabled:
            self.enabled = False
            self.sideFacing = random.randrange(1, self.sides + 1)
            return True
        return False
