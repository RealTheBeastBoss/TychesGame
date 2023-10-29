import pygame
import random
from square import Square
from card import *


class ScreenState(Enum):
    START = 1
    NEW_MENU = 2
    PLAYER_NAMING = 3
    GAME_INTRO_ONE = 4
    GAME_INTRO_TWO = 5
    BLUE_CARD_GUIDE = 6
    RED_CARD_GUIDE = 7
    BOARD_SYMBOLS_GUIDE_ONE = 8
    BOARD_SYMBOLS_GUIDE_TWO = 9
    PLAYING_GAME = 10
    JOIN_LOCAL_GAME = 11
    NAME_LOCAL_PLAYER = 12
    CREATE_SERVER = 13
    PLAYING_LOCAL_GAME = 14


class TurnStage(Enum):
    START_TURN = 0
    ROLL_DICE = 1
    MOVEMENT = 2
    SQUARE_ACTION = 3
    DRAW_CARDS = 4
    ATTACK_MONSTER = 5
    MONSTER_ATTACK = 6
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
D4_ONE = (pygame.image.load(os.path.join("Assets", "Dice", "d4_one.png")), (43, 39))
D4_TWO = (pygame.image.load(os.path.join("Assets", "Dice", "d4_two.png")), (43, 39))
D4_THREE = (pygame.image.load(os.path.join("Assets", "Dice", "d4_three.png")), (43, 39))
D4_FOUR = (pygame.image.load(os.path.join("Assets", "Dice", "d4_four.png")), (43, 39))
D6_ONE = (pygame.image.load(os.path.join("Assets", "Dice", "d6_one.png")), (42, 42))
D6_TWO = (pygame.image.load(os.path.join("Assets", "Dice", "d6_two.png")), (42, 42))
D6_THREE = (pygame.image.load(os.path.join("Assets", "Dice", "d6_three.png")), (42, 42))
D6_FOUR = (pygame.image.load(os.path.join("Assets", "Dice", "d6_four.png")), (42, 42))
D6_FIVE = (pygame.image.load(os.path.join("Assets", "Dice", "d6_five.png")), (42, 42))
D6_SIX = (pygame.image.load(os.path.join("Assets", "Dice", "d6_six.png")), (42, 42))
D8_ONE = (pygame.image.load(os.path.join("Assets", "Dice", "d8_one.png")), (44, 51))
D8_TWO = (pygame.image.load(os.path.join("Assets", "Dice", "d8_two.png")), (44, 51))
D8_THREE = (pygame.image.load(os.path.join("Assets", "Dice", "d8_three.png")), (44, 51))
D8_FOUR = (pygame.image.load(os.path.join("Assets", "Dice", "d8_four.png")), (44, 51))
D8_FIVE = (pygame.image.load(os.path.join("Assets", "Dice", "d8_five.png")), (44, 51))
D8_SIX = (pygame.image.load(os.path.join("Assets", "Dice", "d8_six.png")), (44, 51))
D8_SEVEN = (pygame.image.load(os.path.join("Assets", "Dice", "d8_seven.png")), (44, 51))
D8_EIGHT = (pygame.image.load(os.path.join("Assets", "Dice", "d8_eight.png")), (44, 51))
D12_ONE = (pygame.image.load(os.path.join("Assets", "Dice", "d12_one.png")), (41, 43))
D12_TWO = (pygame.image.load(os.path.join("Assets", "Dice", "d12_two.png")), (41, 43))
D12_THREE = (pygame.image.load(os.path.join("Assets", "Dice", "d12_three.png")), (41, 43))
D12_FOUR = (pygame.image.load(os.path.join("Assets", "Dice", "d12_four.png")), (41, 43))
D12_FIVE = (pygame.image.load(os.path.join("Assets", "Dice", "d12_five.png")), (41, 43))
D12_SIX = (pygame.image.load(os.path.join("Assets", "Dice", "d12_six.png")), (41, 43))
D12_SEVEN = (pygame.image.load(os.path.join("Assets", "Dice", "d12_seven.png")), (41, 43))
D12_EIGHT = (pygame.image.load(os.path.join("Assets", "Dice", "d12_eight.png")), (41, 43))
D12_NINE = (pygame.image.load(os.path.join("Assets", "Dice", "d12_nine.png")), (41, 43))
D12_TEN = (pygame.image.load(os.path.join("Assets", "Dice", "d12_ten.png")), (41, 43))
D12_ELEVEN = (pygame.image.load(os.path.join("Assets", "Dice", "d12_eleven.png")), (41, 43))
D12_TWELVE = (pygame.image.load(os.path.join("Assets", "Dice", "d12_twelve.png")), (41, 43))
D10_ONE = (pygame.image.load(os.path.join("Assets", "Dice", "d10_one.png")), (55, 54))
D10_TWO = (pygame.image.load(os.path.join("Assets", "Dice", "d10_two.png")), (55, 54))
D10_THREE = (pygame.image.load(os.path.join("Assets", "Dice", "d10_three.png")), (55, 54))
D10_FOUR = (pygame.image.load(os.path.join("Assets", "Dice", "d10_four.png")), (55, 54))
D10_FIVE = (pygame.image.load(os.path.join("Assets", "Dice", "d10_five.png")), (55, 54))
D10_SIX = (pygame.image.load(os.path.join("Assets", "Dice", "d10_six.png")), (55, 54))
D10_SEVEN = (pygame.image.load(os.path.join("Assets", "Dice", "d10_seven.png")), (55, 54))
D10_EIGHT = (pygame.image.load(os.path.join("Assets", "Dice", "d10_eight.png")), (55, 54))
D10_NINE = (pygame.image.load(os.path.join("Assets", "Dice", "d10_nine.png")), (55, 54))
D10_TEN = (pygame.image.load(os.path.join("Assets", "Dice", "d10_ten.png")), (55, 54))
D20_ONE = (pygame.image.load(os.path.join("Assets", "Dice", "d20_one.png")), (46, 52))
D20_TWO = (pygame.image.load(os.path.join("Assets", "Dice", "d20_two.png")), (46, 52))
D20_THREE = (pygame.image.load(os.path.join("Assets", "Dice", "d20_three.png")), (46, 52))
D20_FOUR = (pygame.image.load(os.path.join("Assets", "Dice", "d20_four.png")), (46, 52))
D20_FIVE = (pygame.image.load(os.path.join("Assets", "Dice", "d20_five.png")), (46, 52))
D20_SIX = (pygame.image.load(os.path.join("Assets", "Dice", "d20_six.png")), (46, 52))
D20_SEVEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_seven.png")), (46, 52))
D20_EIGHT = (pygame.image.load(os.path.join("Assets", "Dice", "d20_eight.png")), (46, 52))
D20_NINE = (pygame.image.load(os.path.join("Assets", "Dice", "d20_nine.png")), (46, 52))
D20_TEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_ten.png")), (46, 52))
D20_ELEVEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_eleven.png")), (46, 52))
D20_TWELVE = (pygame.image.load(os.path.join("Assets", "Dice", "d20_twelve.png")), (46, 52))
D20_THIRTEEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_thirteen.png")), (46, 52))
D20_FOURTEEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_fourteen.png")), (46, 52))
D20_FIFTEEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_fifteen.png")), (46, 52))
D20_SIXTEEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_sixteen.png")), (46, 52))
D20_SEVENTEEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_seventeen.png")), (46, 52))
D20_EIGHTEEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_eighteen.png")), (46, 52))
D20_NINETEEN = (pygame.image.load(os.path.join("Assets", "Dice", "d20_nineteen.png")), (46, 52))
D20_TWENTY = (pygame.image.load(os.path.join("Assets", "Dice", "d20_twenty.png")), (46, 52))
BLUE_CARD_SYMBOL = (pygame.image.load(os.path.join("Assets", "Cards", "blue_back.png")), (68, 100))
RED_CARD_SYMBOL = (pygame.image.load(os.path.join("Assets", "Cards", "red_back.png")), (68, 100))
GAME_TITLE = (pygame.image.load(os.path.join("Assets", "Text", "title.png")), (617, 95))
# Board Symbols
ONE_BLUE = pygame.image.load(os.path.join("Assets", "Symbols", "one_blue.png"))
ONE_RED = pygame.image.load(os.path.join("Assets", "Symbols", "one_red.png"))
MISS_TURN = pygame.image.load(os.path.join("Assets", "Symbols", "miss_turn.png"))
MONSTER = pygame.image.load(os.path.join("Assets", "Symbols", "monster.png"))
TWO_BLUE = pygame.image.load(os.path.join("Assets", "Symbols", "two_blue.png"))
TWO_RED = pygame.image.load(os.path.join("Assets", "Symbols", "two_red.png"))
GO_BACK = pygame.image.load(os.path.join("Assets", "Symbols", "go_back.png"))
REDO = pygame.image.load(os.path.join("Assets", "Symbols", "redo.png"))
BLUE_RED = pygame.image.load(os.path.join("Assets", "Symbols", "blue_red.png"))
DOWN_KEY = pygame.image.load(os.path.join("Assets", "Symbols", "down_key.png"))
UP_KEY = pygame.image.load(os.path.join("Assets", "Symbols", "up_key.png"))
BACK_8 = pygame.image.load(os.path.join("Assets", "Symbols", "back_8.png"))
ROLL_8 = pygame.image.load(os.path.join("Assets", "Symbols", "roll_8.png"))
BACK_10 = pygame.image.load(os.path.join("Assets", "Symbols", "back_10.png"))
ROLL_10 = pygame.image.load(os.path.join("Assets", "Symbols", "roll_10.png"))
NICE_HAND = pygame.image.load(os.path.join("Assets", "Symbols", "nice_hand.png"))
GRAVITY_WELL = pygame.image.load(os.path.join("Assets", "Symbols", "gravity_well.png"))
ID_TO_SYMBOLS = {
    "OneBlue": ONE_BLUE,
    "OneRed": ONE_RED,
    "MissTurn": MISS_TURN,
    "Monster": MONSTER,
    "TwoBlue": TWO_BLUE,
    "TwoRed": TWO_RED,
    "GoBack": GO_BACK,
    "Redo": REDO,
    "BlueRed": BLUE_RED,
    "DownKey": DOWN_KEY,
    "UpKey": UP_KEY,
    "Back8": BACK_8,
    "Roll8": ROLL_8,
    "Back10": BACK_10,
    "Roll10": ROLL_10,
    "NiceHand": NICE_HAND,
    "GravityWell": GRAVITY_WELL
}

# Game Cards
# region
BLUE_ACE_OF_HEARTS = Card("Blue Ace of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.ACE, "ace_hearts.png", (382, 92),
                          "Use this card to swap with a non-Joker", "card on top of the Discard Pile")
BLUE_TWO_OF_HEARTS = Card("Blue Two of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.TWO, "2_hearts.png", (340, 70),
                          "Roll your next dice with advantage")
BLUE_THREE_OF_HEARTS = Card("Blue Three of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.THREE, "3_hearts.png", (352, 92),
                            "Other Player(s) get 1 Red Card, but", "you must choose one to spare")
BLUE_FOUR_OF_HEARTS = Card("Blue Four of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.FOUR, "4_hearts.png", (360, 92),
                           "Add a d4 Elemental Damage to your", "next Attack Roll")
BLUE_FIVE_OF_HEARTS = Card("Blue Five of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.FIVE, "5_hearts.png", (280, 92),
                           "You can choose the value of", "someone's next d6 Roll")
BLUE_SIX_OF_HEARTS = Card("Blue Six of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.SIX, "6_hearts.png", (365, 70),
                          "Blocks Forced Backwards Movement")
BLUE_SEVEN_OF_HEARTS = Card("Blue Seven of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.SEVEN, "7_hearts.png")
BLUE_EIGHT_OF_HEARTS = Card("Blue Eight of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.EIGHT, "8_hearts.png", (425, 92),
                            "Use this card as a shield against a Monster", "(Used Automatically when Failed Defence)")
BLUE_NINE_OF_HEARTS = Card("Blue Nine of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.NINE, "9_hearts.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_HEARTS = Card("Blue Ten of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.TEN, "10_hearts.png", (295, 114),
                          "Sneak through the next Magic", "Barrier you come across", "(Used Automatically)")
BLUE_JACK_OF_HEARTS = Card("Blue Jack of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.JACK, "jack_hearts.png", (392, 70),
                                     "Make your next Movement Roll with 2 d6")
BLUE_KING_OF_HEARTS = Card("Blue King of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.KING, "king_hearts.png")
BLUE_QUEEN_OF_HEARTS = Card("Blue Queen of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.QUEEN, "queen_hearts.png", (437, 70),
                            "Use this card to not draw a set of Red Cards")
BLUE_ACE_OF_DIAMONDS = Card("Blue Ace of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.ACE, "ace_diamonds.png",
                            (382, 92), "Use this card to swap with a non-Joker", "card on top of the Discard Pile")
BLUE_TWO_OF_DIAMONDS = Card("Blue Two of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.TWO, "2_diamonds.png", (340, 70),
                          "Roll your next dice with advantage")
BLUE_THREE_OF_DIAMONDS = Card("Blue Three of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.THREE, "3_diamonds.png", (352, 92),
                            "Other Player(s) get 1 Red Card, but", "you must choose one to spare")
BLUE_FOUR_OF_DIAMONDS = Card("Blue Four of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.FOUR, "4_diamonds.png", (360, 92),
                           "Add a d4 Elemental Damage to your", "next Attack Roll")
BLUE_FIVE_OF_DIAMONDS = Card("Blue Five of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.FIVE, "5_diamonds.png", (280, 92),
                           "You can choose the value of", "someone's next d6 Roll")
BLUE_SIX_OF_DIAMONDS = Card("Blue Six of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.SIX, "6_diamonds.png", (365, 70),
                          "Blocks Forced Backwards Movement")
BLUE_SEVEN_OF_DIAMONDS = Card("Blue Seven of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.SEVEN, "7_diamonds.png")
BLUE_EIGHT_OF_DIAMONDS = Card("Blue Eight of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.EIGHT, "8_diamonds.png", (425, 92),
                            "Use this card as a shield against a Monster", "(Used Automatically when Failed Defence)")
BLUE_NINE_OF_DIAMONDS = Card("Blue Nine of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.NINE, "9_diamonds.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_DIAMONDS = Card("Blue Ten of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.TEN, "10_diamonds.png", (295, 114),
                          "Sneak through the next Magic", "Barrier you come across", "(Used Automatically)")
BLUE_JACK_OF_DIAMONDS = Card("Blue Jack of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.JACK, "jack_diamonds.png", (392, 70),
                                     "Make your next Movement Roll with 2 d6")
BLUE_KING_OF_DIAMONDS = Card("Blue King of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.KING, "king_diamonds.png")
BLUE_QUEEN_OF_DIAMONDS = Card("Blue Queen of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.QUEEN, "queen_diamonds.png", (437, 70),
                            "Use this card to not draw a set of Red Cards")
BLUE_ACE_OF_CLUBS = Card("Blue Ace of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.ACE, "ace_clubs.png", (382, 92),
                          "Use this card to swap with a non-Joker", "card on top of the Discard Pile")
BLUE_TWO_OF_CLUBS = Card("Blue Two of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.TWO, "2_clubs.png", (340, 70),
                          "Roll your next dice with advantage")
BLUE_THREE_OF_CLUBS = Card("Blue Three of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.THREE, "3_clubs.png", (352, 92),
                            "Other Player(s) get 1 Red Card, but", "you must choose one to spare")
BLUE_FOUR_OF_CLUBS = Card("Blue Four of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.FOUR, "4_clubs.png", (360, 92),
                           "Add a d4 Elemental Damage to your", "next Attack Roll")
BLUE_FIVE_OF_CLUBS = Card("Blue Five of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.FIVE, "5_clubs.png", (280, 92),
                           "You can choose the value of", "someone's next d6 Roll")
BLUE_SIX_OF_CLUBS = Card("Blue Six of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.SIX, "6_clubs.png", (365, 70),
                          "Blocks Forced Backwards Movement")
BLUE_SEVEN_OF_CLUBS = Card("Blue Seven of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.SEVEN, "7_clubs.png")
BLUE_EIGHT_OF_CLUBS = Card("Blue Eight of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.EIGHT, "8_clubs.png", (425, 92),
                            "Use this card as a shield against a Monster", "(Used Automatically when Failed Defence)")
BLUE_NINE_OF_CLUBS = Card("Blue Nine of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.NINE, "9_clubs.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_CLUBS = Card("Blue Ten of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.TEN, "10_clubs.png", (295, 114),
                          "Sneak through the next Magic", "Barrier you come across", "(Used Automatically)")
BLUE_JACK_OF_CLUBS = Card("Blue Jack of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.JACK, "jack_clubs.png", (392, 70),
                                     "Make your next Movement Roll with 2 d6")
BLUE_KING_OF_CLUBS = Card("Blue King of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.KING, "king_clubs.png")
BLUE_QUEEN_OF_CLUBS = Card("Blue Queen of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.QUEEN, "queen_clubs.png", (437, 70),
                            "Use this card to not draw a set of Red Cards")
BLUE_ACE_OF_SPADES = Card("Blue Ace of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.ACE, "ace_spades.png", (382, 92),
                          "Use this card to swap with a non-Joker", "card on top of the Discard Pile")
BLUE_TWO_OF_SPADES = Card("Blue Two of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.TWO, "2_spades.png", (340, 70),
                          "Roll your next dice with advantage")
BLUE_THREE_OF_SPADES = Card("Blue Three of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.THREE, "3_spades.png", (352, 92),
                            "Other Player(s) get 1 Red Card, but", "you must choose one to spare")
BLUE_FOUR_OF_SPADES = Card("Blue Four of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.FOUR, "4_spades.png", (360, 92),
                           "Add a d4 Elemental Damage to your", "next Attack Roll")
BLUE_FIVE_OF_SPADES = Card("Blue Five of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.FIVE, "5_spades.png", (280, 92),
                           "You can choose the value of", "someone's next d6 Roll")
BLUE_SIX_OF_SPADES = Card("Blue Six of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.SIX, "6_spades.png", (365, 70),
                          "Blocks Forced Backwards Movement")
BLUE_SEVEN_OF_SPADES = Card("Blue Seven of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.SEVEN, "7_spades.png")
BLUE_EIGHT_OF_SPADES = Card("Blue Eight of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.EIGHT, "8_spades.png", (425, 92),
                            "Use this card as a shield against a Monster", "(Used Automatically when Failed Defence)")
BLUE_NINE_OF_SPADES = Card("Blue Nine of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.NINE, "9_spades.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_SPADES = Card("Blue Ten of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.TEN, "10_spades.png", (295, 114),
                          "Sneak through the next Magic", "Barrier you come across", "(Used Automatically)")
BLUE_JACK_OF_SPADES = Card("Blue Jack of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.JACK, "jack_spades.png", (392, 70),
                                     "Make your next Movement Roll with 2 d6")
BLUE_KING_OF_SPADES = Card("Blue King of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.KING, "king_spades.png")
BLUE_QUEEN_OF_SPADES = Card("Blue Queen of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.QUEEN, "queen_spades.png", (437, 70),
                            "Use this card to not draw a set of Red Cards")
BLUE_RED_JOKER = Card("Blue Coloured Joker", CardType.BLUE, CardSuit.RED, CardValue.JOKER, "red_joker.png")
BLUE_BLACK_JOKER = Card("Blue Gray Joker", CardType.BLUE, CardSuit.BLACK, CardValue.JOKER, "black_joker.png")
RED_ACE_OF_HEARTS = Card("Red Ace of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.ACE, "ace_hearts.png")
RED_TWO_OF_HEARTS = Card("Red Two of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.TWO, "2_hearts.png", (368, 70),
                          "Roll your next dice with disadvantage")
RED_THREE_OF_HEARTS = Card("Red Three of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.THREE, "3_hearts.png", (358, 92),
                            "Other Player(s) get 1 Blue Card, but", "you must choose one to miss out")
RED_FOUR_OF_HEARTS = Card("Red Four of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.FOUR, "4_hearts.png", (355, 92),
                           "Subtract a d4 from your next Attack", "Roll, you've been poisoned")
RED_FIVE_OF_HEARTS = Card("Red Five of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.FIVE, "5_hearts.png", (280, 92),
                           "Someone chooses the value", "of your next d6 Roll")
RED_SIX_OF_HEARTS = Card("Red Six of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.SIX, "6_hearts.png", (290, 70),
                         "Blocks next Bonus Movement")
RED_SEVEN_OF_HEARTS = Card("Red Seven of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.SEVEN, "7_hearts.png")
RED_EIGHT_OF_HEARTS = Card("Red Eight of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.EIGHT, "8_hearts.png", (335, 70),
                           "Lowers a successful defence to 2")
RED_NINE_OF_HEARTS = Card("Red Nine of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.NINE, "9_hearts.png", (270, 92),
                          "Other Players agree where", "to put a Magic Barrier")
RED_TEN_OF_HEARTS = Card("Red Ten of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.TEN, "10_hearts.png")
RED_JACK_OF_HEARTS = Card("Red Jack of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.JACK, "jack_hearts.png", (392, 70),
                                     "Make your next Movement Roll with 1 d4")
RED_KING_OF_HEARTS = Card("Red King of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.KING, "king_hearts.png")
RED_QUEEN_OF_HEARTS = Card("Red Queen of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.QUEEN, "queen_hearts.png", (248, 92),
                           "Blocks you from drawing", "next set of Blue Cards")
RED_ACE_OF_DIAMONDS = Card("Red Ace of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.ACE, "ace_diamonds.png")
RED_TWO_OF_DIAMONDS = Card("Red Two of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.TWO, "2_diamonds.png", (368, 70),
                          "Roll your next dice with disadvantage")
RED_THREE_OF_DIAMONDS = Card("Red Three of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.THREE, "3_diamonds.png", (358, 92),
                            "Other Player(s) get 1 Blue Card, but", "you must choose one to miss out")
RED_FOUR_OF_DIAMONDS = Card("Red Four of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.FOUR, "4_diamonds.png", (355, 92),
                           "Subtract a d4 from your next Attack", "Roll, you've been poisoned")
RED_FIVE_OF_DIAMONDS = Card("Red Five of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.FIVE, "5_diamonds.png", (280, 92),
                           "Someone chooses the value", "of your next d6 Roll")
RED_SIX_OF_DIAMONDS = Card("Red Six of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.SIX, "6_diamonds.png", (290, 70),
                         "Blocks next Bonus Movement")
RED_SEVEN_OF_DIAMONDS = Card("Red Seven of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.SEVEN, "7_diamonds.png")
RED_EIGHT_OF_DIAMONDS = Card("Red Eight of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.EIGHT, "8_diamonds.png", (335, 70),
                           "Lowers a successful defence to 2")
RED_NINE_OF_DIAMONDS = Card("Red Nine of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.NINE, "9_diamonds.png", (270, 92),
                          "Other Players agree where", "to put a Magic Barrier")
RED_TEN_OF_DIAMONDS = Card("Red Ten of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.TEN, "10_diamonds.png")
RED_JACK_OF_DIAMONDS = Card("Red Jack of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.JACK, "jack_diamonds.png", (392, 70),
                                     "Make your next Movement Roll with 1 d4")
RED_KING_OF_DIAMONDS = Card("Red King of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.KING, "king_diamonds.png")
RED_QUEEN_OF_DIAMONDS = Card("Red Queen of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.QUEEN, "queen_diamonds.png", (248, 92),
                           "Blocks you from drawing", "next set of Blue Cards")
RED_ACE_OF_CLUBS = Card("Red Ace of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.ACE, "ace_clubs.png")
RED_TWO_OF_CLUBS = Card("Red Two of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.TWO, "2_clubs.png", (368, 70),
                          "Roll your next dice with disadvantage")
RED_THREE_OF_CLUBS = Card("Red Three of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.THREE, "3_clubs.png", (358, 92),
                            "Other Player(s) get 1 Blue Card, but", "you must choose one to miss out")
RED_FOUR_OF_CLUBS = Card("Red Four of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.FOUR, "4_clubs.png", (355, 92),
                           "Subtract a d4 from your next Attack", "Roll, you've been poisoned")
RED_FIVE_OF_CLUBS = Card("Red Five of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.FIVE, "5_clubs.png", (280, 92),
                           "Someone chooses the value", "of your next d6 Roll")
RED_SIX_OF_CLUBS = Card("Red Six of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.SIX, "6_clubs.png", (290, 70),
                         "Blocks next Bonus Movement")
RED_SEVEN_OF_CLUBS = Card("Red Seven of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.SEVEN, "7_clubs.png")
RED_EIGHT_OF_CLUBS = Card("Red Eight of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.EIGHT, "8_clubs.png", (335, 70),
                           "Lowers a successful defence to 2")
RED_NINE_OF_CLUBS = Card("Red Nine of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.NINE, "9_clubs.png", (270, 92),
                          "Other Players agree where", "to put a Magic Barrier")
RED_TEN_OF_CLUBS = Card("Red Ten of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.TEN, "10_clubs.png")
RED_JACK_OF_CLUBS = Card("Red Jack of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.JACK, "jack_clubs.png", (392, 70),
                                     "Make your next Movement Roll with 1 d4")
RED_KING_OF_CLUBS = Card("Red King of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.KING, "king_clubs.png")
RED_QUEEN_OF_CLUBS = Card("Red Queen of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.QUEEN, "queen_clubs.png", (248, 92),
                           "Blocks you from drawing", "next set of Blue Cards")
RED_ACE_OF_SPADES = Card("Red Ace of Spades", CardType.RED, CardSuit.SPADES, CardValue.ACE, "ace_spades.png")
RED_TWO_OF_SPADES = Card("Red Two of Spades", CardType.RED, CardSuit.SPADES, CardValue.TWO, "2_spades.png", (368, 70),
                          "Roll your next dice with disadvantage")
RED_THREE_OF_SPADES = Card("Red Three of Spades", CardType.RED, CardSuit.SPADES, CardValue.THREE, "3_spades.png", (358, 92),
                            "Other Player(s) get 1 Blue Card, but", "you must choose one to miss out")
RED_FOUR_OF_SPADES = Card("Red Four of Spades", CardType.RED, CardSuit.SPADES, CardValue.FOUR, "4_spades.png", (355, 92),
                           "Subtract a d4 from your next Attack", "Roll, you've been poisoned")
RED_FIVE_OF_SPADES = Card("Red Five of Spades", CardType.RED, CardSuit.SPADES, CardValue.FIVE, "5_spades.png", (280, 92),
                           "Someone chooses the value", "of your next d6 Roll")
RED_SIX_OF_SPADES = Card("Red Six of Spades", CardType.RED, CardSuit.SPADES, CardValue.SIX, "6_spades.png", (290, 70),
                         "Blocks next Bonus Movement")
RED_SEVEN_OF_SPADES = Card("Red Seven of Spades", CardType.RED, CardSuit.SPADES, CardValue.SEVEN, "7_spades.png")
RED_EIGHT_OF_SPADES = Card("Red Eight of Spades", CardType.RED, CardSuit.SPADES, CardValue.EIGHT, "8_spades.png", (335, 70),
                           "Lowers a successful defence to 2")
RED_NINE_OF_SPADES = Card("Red Nine of Spades", CardType.RED, CardSuit.SPADES, CardValue.NINE, "9_spades.png", (270, 92),
                          "Other Players agree where", "to put a Magic Barrier")
RED_TEN_OF_SPADES = Card("Red Ten of Spades", CardType.RED, CardSuit.SPADES, CardValue.TEN, "10_spades.png")
RED_JACK_OF_SPADES = Card("Red Jack of Spades", CardType.RED, CardSuit.SPADES, CardValue.JACK, "jack_spades.png", (392, 70),
                                     "Make your next Movement Roll with 1 d4")
RED_KING_OF_SPADES = Card("Red King of Spades", CardType.RED, CardSuit.SPADES, CardValue.KING, "king_spades.png")
RED_QUEEN_OF_SPADES = Card("Red Queen of Spades", CardType.RED, CardSuit.SPADES, CardValue.QUEEN, "queen_spades.png", (248, 92),
                           "Blocks you from drawing", "next set of Blue Cards")
RED_RED_JOKER = Card("Red Coloured Joker", CardType.RED, CardSuit.RED, CardValue.JOKER, "red_joker.png")
RED_BLACK_JOKER = Card("Red Gray Joker", CardType.RED, CardSuit.BLACK, CardValue.JOKER, "black_joker.png")
# endregion

pygame.font.init()
# Unchangeable Global Variables
FPS = 60
BIGGER_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 120)
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
PLAYER_TO_PIECE = {
    0: PLAYER_ONE,
    1: PLAYER_TWO,
    2: PLAYER_THREE,
    3: PLAYER_FOUR,
    4: PLAYER_FIVE
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
D4_IMAGES = {
    1: D4_ONE,
    2: D4_TWO,
    3: D4_THREE,
    4: D4_FOUR
}
D6_IMAGES = {
    1: D6_ONE,
    2: D6_TWO,
    3: D6_THREE,
    4: D6_FOUR,
    5: D6_FIVE,
    6: D6_SIX
}
D12_IMAGES = {
    1: D12_ONE,
    2: D12_TWO,
    3: D12_THREE,
    4: D12_FOUR,
    5: D12_FIVE,
    6: D12_SIX,
    7: D12_SEVEN,
    8: D12_EIGHT,
    9: D12_NINE,
    10: D12_TEN,
    11: D12_ELEVEN,
    12: D12_TWELVE
}
D10_IMAGES = {
    1: D10_ONE,
    2: D10_TWO,
    3: D10_THREE,
    4: D10_FOUR,
    5: D10_FIVE,
    6: D10_SIX,
    7: D10_SEVEN,
    8: D10_EIGHT,
    9: D10_NINE,
    10: D10_TEN
}
D8_IMAGES = {
    1: D8_ONE,
    2: D8_TWO,
    3: D8_THREE,
    4: D8_FOUR,
    5: D8_FIVE,
    6: D8_SIX,
    7: D8_SEVEN,
    8: D8_EIGHT
}
D20_IMAGES = {
    1: D20_ONE,
    2: D20_TWO,
    3: D20_THREE,
    4: D20_FOUR,
    5: D20_FIVE,
    6: D20_SIX,
    7: D20_SEVEN,
    8: D20_EIGHT,
    9: D20_NINE,
    10: D20_TEN,
    11: D20_ELEVEN,
    12: D20_TWELVE,
    13: D20_THIRTEEN,
    14: D20_FOURTEEN,
    15: D20_FIFTEEN,
    16: D20_SIXTEEN,
    17: D20_SEVENTEEN,
    18: D20_EIGHTEEN,
    19: D20_NINETEEN,
    20: D20_TWENTY,
}
ALLOWED_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                pygame.K_BACKSLASH, pygame.K_BACKSPACE, pygame.K_COMMA, pygame.K_QUESTION, pygame.K_SPACE, pygame.K_RETURN, pygame.K_PERIOD]


class Meta:  # Changeable Global Variables
    # Local Game Things
    IS_MULTIPLAYER = False
    NETWORK = None
    HAS_SERVER = False
    PLAYER_NUMBER = 69
    EVENT_LIST = []
    SQUARE_VOTE = False
    # Regular Variables
    DEBUG_INFO = []
    PLAYER_COUNT = None
    CURRENT_STATE = ScreenState.START
    TURN_STAGE = TurnStage.START_TURN
    PLAYERS = []
    CURRENT_PLAYER = 0
    CAN_TEXT_INPUT = False
    USER_TEXT = ""
    HOVER_BOXES = []
    CARD_HANDS_ACTIVE = True
    SHOW_HAND = None
    CARD_TO_REMOVE = None
    ROLLING_WITH_ADVANTAGE = False
    ROLLING_WITH_DISADVANTAGE = False
    ROLLING_DOUBLE = False
    DICE_ROLLED = 0
    SQUARES_TO_MOVE = 0
    TOP_DICE = []
    MIDDLE_DICE = []
    BOTTOM_DICE = []
    CHOOSE_PLAYERS = None
    CHOSEN_PLAYER = None
    CHOOSE_DICE = None
    CHOOSE_SQUARE = None
    CARDS_TO_DRAW = []
    DISPLAYING_CARD = False
    SUCCEEDED_DEFENCE = None
    FORCED_CARD = None
    ADDING_FOUR = False
    TAKING_FOUR = False
    TAKEN_FOUR = False
    SHIELD_ACTIVE = False
    ROLLING_WITH_FOUR = False
    FORCED_MOVEMENT = False
    BONUS_MOVEMENT = False
    # Global Events
    TEXT_CONFIRMED = False
    BUTTONS_ENABLED = True
    LEFT_MOUSE_RELEASED = False
    LEFT_ARROW_DOWN = False
    RIGHT_ARROW_DOWN = False
    # Big Lists
    DISCARD_PILE = []
    RED_DRAW_DECK = [RED_ACE_OF_HEARTS, RED_TWO_OF_HEARTS, RED_THREE_OF_HEARTS, RED_FOUR_OF_HEARTS, RED_FIVE_OF_HEARTS,
                     RED_SIX_OF_HEARTS,
                     RED_SEVEN_OF_HEARTS, RED_EIGHT_OF_HEARTS, RED_NINE_OF_HEARTS, RED_TEN_OF_HEARTS,
                     RED_JACK_OF_HEARTS, RED_KING_OF_HEARTS,
                     RED_QUEEN_OF_HEARTS, RED_ACE_OF_DIAMONDS, RED_TWO_OF_DIAMONDS, RED_THREE_OF_DIAMONDS,
                     RED_FOUR_OF_DIAMONDS, RED_FIVE_OF_DIAMONDS,
                     RED_SIX_OF_DIAMONDS, RED_SEVEN_OF_DIAMONDS, RED_EIGHT_OF_DIAMONDS, RED_NINE_OF_DIAMONDS,
                     RED_TEN_OF_DIAMONDS, RED_JACK_OF_DIAMONDS,
                     RED_KING_OF_DIAMONDS, RED_QUEEN_OF_DIAMONDS, RED_ACE_OF_CLUBS, RED_TWO_OF_CLUBS,
                     RED_THREE_OF_CLUBS, RED_FOUR_OF_CLUBS,
                     RED_FIVE_OF_CLUBS, RED_SIX_OF_CLUBS, RED_SEVEN_OF_CLUBS, RED_EIGHT_OF_CLUBS, RED_NINE_OF_CLUBS,
                     RED_TEN_OF_CLUBS,
                     RED_JACK_OF_CLUBS, RED_KING_OF_CLUBS, RED_QUEEN_OF_CLUBS, RED_ACE_OF_SPADES, RED_TWO_OF_SPADES,
                     RED_THREE_OF_SPADES,
                     RED_FOUR_OF_SPADES, RED_FIVE_OF_SPADES, RED_SIX_OF_SPADES, RED_SEVEN_OF_SPADES,
                     RED_EIGHT_OF_SPADES, RED_NINE_OF_SPADES,
                     RED_TEN_OF_SPADES, RED_JACK_OF_SPADES, RED_KING_OF_SPADES, RED_QUEEN_OF_SPADES, RED_BLACK_JOKER,
                     RED_RED_JOKER]
    random.shuffle(RED_DRAW_DECK)
    BLUE_DRAW_DECK = [BLUE_ACE_OF_HEARTS, BLUE_TWO_OF_HEARTS, BLUE_THREE_OF_HEARTS, BLUE_FOUR_OF_HEARTS,
                      BLUE_FIVE_OF_HEARTS, BLUE_SIX_OF_HEARTS,
                      BLUE_SEVEN_OF_HEARTS, BLUE_EIGHT_OF_HEARTS, BLUE_NINE_OF_HEARTS, BLUE_TEN_OF_HEARTS,
                      BLUE_JACK_OF_HEARTS, BLUE_KING_OF_HEARTS,
                      BLUE_QUEEN_OF_HEARTS, BLUE_ACE_OF_DIAMONDS, BLUE_TWO_OF_DIAMONDS, BLUE_THREE_OF_DIAMONDS,
                      BLUE_FOUR_OF_DIAMONDS, BLUE_FIVE_OF_DIAMONDS,
                      BLUE_SIX_OF_DIAMONDS, BLUE_SEVEN_OF_DIAMONDS, BLUE_EIGHT_OF_DIAMONDS, BLUE_NINE_OF_DIAMONDS,
                      BLUE_TEN_OF_DIAMONDS, BLUE_JACK_OF_DIAMONDS,
                      BLUE_KING_OF_DIAMONDS, BLUE_QUEEN_OF_DIAMONDS, BLUE_ACE_OF_CLUBS, BLUE_TWO_OF_CLUBS,
                      BLUE_THREE_OF_CLUBS, BLUE_FOUR_OF_CLUBS,
                      BLUE_FIVE_OF_CLUBS, BLUE_SIX_OF_CLUBS, BLUE_SEVEN_OF_CLUBS, BLUE_EIGHT_OF_CLUBS,
                      BLUE_NINE_OF_CLUBS, BLUE_TEN_OF_CLUBS,
                      BLUE_JACK_OF_CLUBS, BLUE_KING_OF_CLUBS, BLUE_QUEEN_OF_CLUBS, BLUE_ACE_OF_SPADES,
                      BLUE_TWO_OF_SPADES, BLUE_THREE_OF_SPADES,
                      BLUE_FOUR_OF_SPADES, BLUE_FIVE_OF_SPADES, BLUE_SIX_OF_SPADES, BLUE_SEVEN_OF_SPADES,
                      BLUE_EIGHT_OF_SPADES, BLUE_NINE_OF_SPADES,
                      BLUE_TEN_OF_SPADES, BLUE_JACK_OF_SPADES, BLUE_KING_OF_SPADES, BLUE_QUEEN_OF_SPADES,
                      BLUE_BLACK_JOKER, BLUE_RED_JOKER]
    random.shuffle(BLUE_DRAW_DECK)
    BOARD_SQUARES = [Square(None, (534, 965)), Square("OneRed", (628, 965)), Square("OneBlue", (722, 965)),
                     Square(None, (816, 965)), Square("OneBlue", (910, 965)), Square(None, (1009, 965)),
                     Square("OneBlue", (1103, 965)), Square("OneBlue", (1197, 965)), Square(None, (1291, 965)),
                     Square("OneRed", (1385, 965)), Square("Monster", (1385, 871), False, 6),
                     Square("MissTurn", (1291, 871)),
                     Square(None, (1197, 871)), Square("TwoRed", (1103, 871)), Square(None, (1009, 871)),
                     Square(None, (910, 871)), Square("GoBack", (816, 871)), Square("Redo", (722, 871)),
                     Square(None, (628, 871)), Square("TwoBlue", (534, 871)), Square(None, (534, 777)),
                     Square("Monster", (628, 777), False, 12), Square(None, (722, 777)), Square("BlueRed", (816, 777)),
                     Square("DownKey", (910, 777), False, 0, 15), Square("UpKey", (1009, 777), False, 0, 34),
                     Square(None, (1103, 777)),
                     Square("Back8", (1197, 777)), Square("Roll8", (1291, 777)), Square(None, (1385, 777)),
                     Square("GravityWell", (1385, 683)), Square(None, (1291, 683)), Square(None, (1197, 683)),
                     Square(None, (1103, 683)), Square(None, (1009, 683)), Square(None, (910, 683)),
                     Square(None, (816, 683)), Square(None, (722, 683)), Square("Back10", (628, 683)),
                     Square("Roll10", (534, 683)), Square(None, (534, 589)), Square(None, (628, 589)),
                     Square(None, (722, 589)), Square(None, (816, 589)), Square(None, (910, 589)),
                     Square(None, (1009, 589)), Square(None, (1103, 589)), Square(None, (1197, 589)),
                     Square(None, (1291, 589)), Square(None, (1385, 589)), Square(None, (1385, 490)),
                     Square(None, (1291, 490)), Square(None, (1197, 490)), Square(None, (1103, 490)),
                     Square(None, (1009, 490)), Square(None, (910, 490)), Square(None, (816, 490)),
                     Square(None, (722, 490)), Square(None, (628, 490)), Square(None, (534, 490)),
                     Square(None, (534, 396)), Square(None, (628, 396)), Square(None, (722, 396)),
                     Square(None, (816, 396)), Square(None, (910, 396)), Square(None, (1009, 396)),
                     Square(None, (1103, 396)), Square(None, (1197, 396)), Square(None, (1291, 396)),
                     Square("NiceHand", (1385, 396)), Square(None, (1385, 302)), Square(None, (1291, 302)),
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
