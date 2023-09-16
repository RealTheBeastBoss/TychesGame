import pygame
import os
from enum import Enum


class ScreenState(Enum):
    START = 1
    NEW_MENU = 2
    PLAYER_NAMING = 3
    GAME_INTRO_ONE = 4
    GAME_INTRO_TWO = 5
    BLUE_CARD_GUIDE = 6
    RED_CARD_GUIDE = 7
    BOARD_SYMBOLS_GUIDE = 8
    PLAYING_GAME = 9


# Game Colours
BLUE = (0, 0, 255)
ORANGE = (255, 102, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PASTEL_GREEN = (193, 225, 193)


# Game Images
BLUE_CARD_SYMBOL = (os.path.join("Assets", "Cards", "blue_back.png"), (68, 100))
RED_CARD_SYMBOL = (os.path.join("Assets", "Cards", "red_back.png"), (68, 100))


pygame.font.init()
# Unchangeable Global Variables
FPS = 60
BIG_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 90)
MEDIUM_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 60)
SMALL_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 30)
TINY_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 20)
BUTTON_COOLDOWN_EVENT = pygame.USEREVENT + 1
WIDTH, HEIGHT = 1920, 1080
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CARD_SIZE = (68, 100)
DEBUG_MODE = False
ALLOWED_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                pygame.K_BACKSLASH, pygame.K_BACKSPACE, pygame.K_COMMA, pygame.K_QUESTION, pygame.K_SPACE, pygame.K_RETURN]


class Meta:  # Changeable Global Variables
    PLAYER_COUNT = None
    CURRENT_STATE = ScreenState.START
    PLAYERS = []
    CURRENT_PLAYER = 0
    CAN_TEXT_INPUT = False
    USER_TEXT = ""
    HOVER_BOXES = []
    # Global Events
    TEXT_CONFIRMED = False
    BUTTONS_ENABLED = True
    LEFT_MOUSE_RELEASED = False
    LEFT_ARROW_DOWN = False
    RIGHT_ARROW_DOWN = False
