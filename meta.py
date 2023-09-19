import pygame
import os
from enum import Enum
from square import Square


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


class TurnStage(Enum):
    ROLL_DICE = 1
    MOVEMENT = 2
    SQUARE_ACTION = 3
    END_TURN = 42
    GAME_WON = 69


# Game Colours
BLUE = (0, 0, 255)
ORANGE = (255, 102, 0)
GREEN = (0, 128, 8)
PINK = (255, 0, 228)
RED = (176, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PASTEL_GREEN = (193, 225, 193)


# Game Images
PLAYER_ONE = pygame.image.load(os.path.join("Assets", "player_one.png"))
PLAYER_TWO = pygame.image.load(os.path.join("Assets", "player_two.png"))
PLAYER_THREE = pygame.image.load(os.path.join("Assets", "player_three.png"))
PLAYER_FOUR = pygame.image.load(os.path.join("Assets", "player_four.png"))
PLAYER_FIVE = pygame.image.load(os.path.join("Assets", "player_five.png"))
D6_ONE = (pygame.image.load(os.path.join("Assets", "Dice", "d6_one.png")), (42, 42))
D6_TWO = (pygame.image.load(os.path.join("Assets", "Dice", "d6_two.png")), (42, 42))
D6_THREE = (pygame.image.load(os.path.join("Assets", "Dice", "d6_three.png")), (42, 42))
D6_FOUR = (pygame.image.load(os.path.join("Assets", "Dice", "d6_four.png")), (42, 42))
D6_FIVE = (pygame.image.load(os.path.join("Assets", "Dice", "d6_five.png")), (42, 42))
D6_SIX = (pygame.image.load(os.path.join("Assets", "Dice", "d6_six.png")), (42, 42))
BLUE_CARD_SYMBOL = (pygame.image.load(os.path.join("Assets", "Cards", "blue_back.png")), (68, 100))
RED_CARD_SYMBOL = (pygame.image.load(os.path.join("Assets", "Cards", "red_back.png")), (68, 100))
# Board Symbols
ONE_BLUE = pygame.image.load(os.path.join("Assets", "Symbols", "one_blue.png"))
ONE_RED = pygame.image.load(os.path.join("Assets", "Symbols", "one_red.png"))
MISS_TURN = pygame.image.load(os.path.join("Assets", "Symbols", "miss_turn.png"))


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
DEBUG_MODE = True
BLUE_DRAW_DECK_RECT = pygame.Rect((258, 100), (204, 300))
RED_DRAW_DECK_RECT = pygame.Rect((258, 500), (204, 300))
PLAYER_TO_POSITION = {
    0: (-25, -25),
    1: (25, -25),
    2: (25, 25),
    3: (-25, 25),
    4: (0, 0)
}
PLAYER_TO_COLOUR = {
    0: BLUE,
    1: ORANGE,
    2: GREEN,
    3: PINK,
    4: RED
}
CARD_TO_POSITION = {
    0: (320, 270),
    1: (640, 270),
    2: (960, 270),
    3: (1280, 270),
    4: (1600, 270),
    5: (320, 540),
    6: (640, 540),
    7: (960, 540),
    8: (1280, 540),
    9: (1600, 540),
    10: (320, 810),
    11: (640, 810),
    12: (960, 810),
    13: (1280, 810),
    14: (1600, 810)
}
D6_IMAGES = {
    1: D6_ONE,
    2: D6_TWO,
    3: D6_THREE,
    4: D6_FOUR,
    5: D6_FIVE,
    6: D6_SIX
}
BOARD_SQUARES = [Square(None, (534, 965)), Square(ONE_RED, (628, 965)), Square(ONE_BLUE, (722, 965)),
                 Square(None, (816, 965)), Square(ONE_BLUE, (910, 965)), Square(None, (1009, 965)),
                 Square(ONE_BLUE, (1103, 965)), Square(ONE_BLUE, (1197, 965)), Square(None, (1291, 965)),
                 Square(ONE_RED, (1385, 965)), Square(MISS_TURN, (1385, 871)), Square(None, (1291, 871)),
                 Square(None, (1197, 871)), Square(None, (1103, 871)), Square(None, (1009, 871)),
                 Square(None, (910, 871)), Square(None, (816, 871)), Square(None, (722, 871)),
                 Square(None, (628, 871)), Square(None, (534, 871)), Square(None, (534, 777)),
                 Square(None, (628, 777)), Square(None, (722, 777)), Square(None, (816, 777)),
                 Square(None, (910, 777)), Square(None, (1009, 777)), Square(None, (1103, 777)),
                 Square(None, (1197, 777)), Square(None, (1291, 777)), Square(None, (1385, 777)),
                 Square(None, (1385, 683)), Square(None, (1291, 683)), Square(None, (1197, 683)),
                 Square(None, (1103, 683)), Square(None, (1009, 683)), Square(None, (910, 683)),
                 Square(None, (816, 683)), Square(None, (722, 683)), Square(None, (628, 683)),
                 Square(None, (534, 683)), Square(None, (534, 589)), Square(None, (628, 589)),
                 Square(None, (722, 589)), Square(None, (816, 589)), Square(None, (910, 589)),
                 Square(None, (1009, 589)), Square(None, (1103, 589)), Square(None, (1197, 589)),
                 Square(None, (1291, 589)), Square(None, (1385, 589)), Square(None, (1385, 490)),
                 Square(None, (1291, 490)), Square(None, (1197, 490)), Square(None, (1103, 490)),
                 Square(None, (1009, 490)), Square(None, (910, 490)), Square(None, (816, 490)),
                 Square(None, (722, 490)), Square(None, (628, 490)), Square(None, (534, 490)),
                 Square(None, (534, 396)), Square(None, (628, 396)), Square(None, (722, 396)),
                 Square(None, (816, 396)), Square(None, (910, 396)), Square(None, (1009, 396)),
                 Square(None, (1103, 396)), Square(None, (1197, 396)), Square(None, (1291, 396)),
                 Square(None, (1385, 396)), Square(None, (1385, 302)), Square(None, (1291, 302)),
                 Square(None, (1197, 302)), Square(None, (1103, 302)), Square(None, (1009, 302)),
                 Square(None, (910, 302)), Square(None, (816, 302)), Square(None, (722, 302)),
                 Square(None, (628, 302)), Square(None, (534, 302)), Square(None, (534, 208)),
                 Square(None, (628, 208)), Square(None, (722, 208)), Square(None, (816, 208)),
                 Square(None, (910, 208)), Square(None, (1009, 208)), Square(None, (1103, 208)),
                 Square(None, (1197, 208)), Square(None, (1291, 208)), Square(None, (1385, 208)),
                 Square(None, (1385, 114)), Square(None, (1291, 114)), Square(None, (1197, 114)),
                 Square(None, (1103, 114)), Square(None, (1009, 114)), Square(None, (910, 114)),
                 Square(None, (816, 114)), Square(None, (722, 114)), Square(None, (628, 114)),
                 Square(None, (534, 114))]
ALLOWED_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                pygame.K_BACKSLASH, pygame.K_BACKSPACE, pygame.K_COMMA, pygame.K_QUESTION, pygame.K_SPACE, pygame.K_RETURN]


class Meta:  # Changeable Global Variables
    DEBUG_INFO = []
    PLAYER_COUNT = None
    CURRENT_STATE = ScreenState.START
    TURN_STAGE = TurnStage.ROLL_DICE
    PLAYERS = []
    CURRENT_PLAYER = 0
    CAN_TEXT_INPUT = False
    USER_TEXT = ""
    HOVER_BOXES = []
    CAN_PROGRESS = False
    CARDS_TO_DRAW = None
    DISPLAY_CARD = None
    CARD_HANDS_ACTIVE = True
    SHOW_HAND = None
    CARD_TO_REMOVE = None
    ROLLING_WITH_ADVANTAGE = False
    ROLLING_WITH_DISADVANTAGE = False
    DICE_ROLLED = 0
    SQUARES_TO_MOVE = 0
    DICE_USED = None
    CHOOSE_PLAYERS = None
    CHOSEN_PLAYER = None
    # Global Events
    TEXT_CONFIRMED = False
    BUTTONS_ENABLED = True
    LEFT_MOUSE_RELEASED = False
    LEFT_ARROW_DOWN = False
    RIGHT_ARROW_DOWN = False
