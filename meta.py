import pygame
import os
from enum import Enum


class ScreenState(Enum):
    START = 1
    NEW_MENU = 2
    PLAYER_NAMING = 3


# Game Colours
BLUE = (0, 0, 255)
ORANGE = (255, 102, 0)


pygame.font.init()
BIG_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 90)
MEDIUM_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 60)
SMALL_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 30)
BUTTON_COOLDOWN_EVENT = pygame.USEREVENT + 1
WIDTH, HEIGHT = 1920, 1080
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
DEBUG_MODE = True


class Meta:
    PLAYER_COUNT = None
    CURRENT_STATE = ScreenState.START
    BUTTONS_ENABLED = True
