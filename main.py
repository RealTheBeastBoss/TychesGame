import random

import pygame.draw

from card import *
from meta import *
from button import Button
from player import Player
from dice import Dice


D6 = Dice(6, D6_IMAGES)


pygame.display.set_caption("Tyche's Game")

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
BLUE_SIX_OF_HEARTS = Card("Blue Six of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.SIX, "6_hearts.png")
BLUE_SEVEN_OF_HEARTS = Card("Blue Seven of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.SEVEN, "7_hearts.png")
BLUE_EIGHT_OF_HEARTS = Card("Blue Eight of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.EIGHT, "8_hearts.png", (425, 70),
                            "Use this card as a shield against a Monster")
BLUE_NINE_OF_HEARTS = Card("Blue Nine of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.NINE, "9_hearts.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_HEARTS = Card("Blue Ten of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.TEN, "10_hearts.png", (295, 92),
                          "Sneak through the next Magic", "Barrier you come across")
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
BLUE_SIX_OF_DIAMONDS = Card("Blue Six of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.SIX, "6_diamonds.png")
BLUE_SEVEN_OF_DIAMONDS = Card("Blue Seven of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.SEVEN, "7_diamonds.png")
BLUE_EIGHT_OF_DIAMONDS = Card("Blue Eight of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.EIGHT, "8_diamonds.png", (425, 70),
                            "Use this card as a shield against a Monster")
BLUE_NINE_OF_DIAMONDS = Card("Blue Nine of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.NINE, "9_diamonds.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_DIAMONDS = Card("Blue Ten of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.TEN, "10_diamonds.png", (295, 92),
                          "Sneak through the next Magic", "Barrier you come across")
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
BLUE_SIX_OF_CLUBS = Card("Blue Six of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.SIX, "6_clubs.png")
BLUE_SEVEN_OF_CLUBS = Card("Blue Seven of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.SEVEN, "7_clubs.png")
BLUE_EIGHT_OF_CLUBS = Card("Blue Eight of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.EIGHT, "8_clubs.png", (425, 70),
                            "Use this card as a shield against a Monster")
BLUE_NINE_OF_CLUBS = Card("Blue Nine of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.NINE, "9_clubs.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_CLUBS = Card("Blue Ten of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.TEN, "10_clubs.png", (295, 92),
                          "Sneak through the next Magic", "Barrier you come across")
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
BLUE_SIX_OF_SPADES = Card("Blue Six of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.SIX, "6_spades.png")
BLUE_SEVEN_OF_SPADES = Card("Blue Seven of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.SEVEN, "7_spades.png")
BLUE_EIGHT_OF_SPADES = Card("Blue Eight of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.EIGHT, "8_spades.png", (425, 70),
                            "Use this card as a shield against a Monster")
BLUE_NINE_OF_SPADES = Card("Blue Nine of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.NINE, "9_spades.png", (250, 92),
                           "Place a Magic Barrier on", "any square you choose")
BLUE_TEN_OF_SPADES = Card("Blue Ten of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.TEN, "10_spades.png", (295, 92),
                          "Sneak through the next Magic", "Barrier you come across")
BLUE_JACK_OF_SPADES = Card("Blue Jack of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.JACK, "jack_spades.png", (392, 70),
                                     "Make your next Movement Roll with 2 d6")
BLUE_KING_OF_SPADES = Card("Blue King of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.KING, "king_spades.png")
BLUE_QUEEN_OF_SPADES = Card("Blue Queen of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.QUEEN, "queen_spades.png", (437, 70),
                            "Use this card to not draw a set of Red Cards")
BLUE_RED_JOKER = Card("Blue Coloured Joker", CardType.BLUE, CardSuit.RED, CardValue.JOKER, "red_joker.png")
BLUE_BLACK_JOKER = Card("Blue Gray Joker", CardType.BLUE, CardSuit.BLACK, CardValue.JOKER, "black_joker.png")
BLUE_DRAW_DECK = [BLUE_ACE_OF_HEARTS, BLUE_TWO_OF_HEARTS, BLUE_THREE_OF_HEARTS, BLUE_FOUR_OF_HEARTS, BLUE_FIVE_OF_HEARTS, BLUE_SIX_OF_HEARTS,
                  BLUE_SEVEN_OF_HEARTS, BLUE_EIGHT_OF_HEARTS, BLUE_NINE_OF_HEARTS, BLUE_TEN_OF_HEARTS, BLUE_JACK_OF_HEARTS, BLUE_KING_OF_HEARTS,
                  BLUE_QUEEN_OF_HEARTS, BLUE_ACE_OF_DIAMONDS, BLUE_TWO_OF_DIAMONDS, BLUE_THREE_OF_DIAMONDS, BLUE_FOUR_OF_DIAMONDS, BLUE_FIVE_OF_DIAMONDS,
                  BLUE_SIX_OF_DIAMONDS, BLUE_SEVEN_OF_DIAMONDS, BLUE_EIGHT_OF_DIAMONDS, BLUE_NINE_OF_DIAMONDS, BLUE_TEN_OF_DIAMONDS, BLUE_JACK_OF_DIAMONDS,
                  BLUE_KING_OF_DIAMONDS, BLUE_QUEEN_OF_DIAMONDS, BLUE_ACE_OF_CLUBS, BLUE_TWO_OF_CLUBS, BLUE_THREE_OF_CLUBS, BLUE_FOUR_OF_CLUBS,
                  BLUE_FIVE_OF_CLUBS, BLUE_SIX_OF_CLUBS, BLUE_SEVEN_OF_CLUBS, BLUE_EIGHT_OF_CLUBS, BLUE_NINE_OF_CLUBS, BLUE_TEN_OF_CLUBS,
                  BLUE_JACK_OF_CLUBS, BLUE_KING_OF_CLUBS, BLUE_QUEEN_OF_CLUBS, BLUE_ACE_OF_SPADES, BLUE_TWO_OF_SPADES, BLUE_THREE_OF_SPADES,
                  BLUE_FOUR_OF_SPADES, BLUE_FIVE_OF_SPADES, BLUE_SIX_OF_SPADES, BLUE_SEVEN_OF_SPADES, BLUE_EIGHT_OF_SPADES, BLUE_NINE_OF_SPADES,
                  BLUE_TEN_OF_SPADES, BLUE_JACK_OF_SPADES, BLUE_KING_OF_SPADES, BLUE_QUEEN_OF_SPADES, BLUE_BLACK_JOKER, BLUE_RED_JOKER]
random.shuffle(BLUE_DRAW_DECK)
RED_ACE_OF_HEARTS = Card("Red Ace of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.ACE, "ace_hearts.png")
RED_TWO_OF_HEARTS = Card("Red Two of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.TWO, "2_hearts.png", (368, 70),
                          "Roll your next dice with disadvantage")
RED_THREE_OF_HEARTS = Card("Red Three of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.THREE, "3_hearts.png", (358, 92),
                            "Other Player(s) get 1 Blue Card, but", "you must choose one to miss out")
RED_FOUR_OF_HEARTS = Card("Red Four of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.FOUR, "4_hearts.png", (355, 92),
                           "Subtract a d4 from your next Attack", "Roll, you've been poisoned")
RED_FIVE_OF_HEARTS = Card("Red Five of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.FIVE, "5_hearts.png", (280, 92),
                           "Someone chooses the value", "of your next d6 Roll")
RED_SIX_OF_HEARTS = Card("Red Six of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.SIX, "6_hearts.png")
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
RED_SIX_OF_DIAMONDS = Card("Red Six of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.SIX, "6_diamonds.png")
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
RED_SIX_OF_CLUBS = Card("Red Six of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.SIX, "6_clubs.png")
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
RED_SIX_OF_SPADES = Card("Red Six of Spades", CardType.RED, CardSuit.SPADES, CardValue.SIX, "6_spades.png")
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
RED_DRAW_DECK = [RED_ACE_OF_HEARTS, RED_TWO_OF_HEARTS, RED_THREE_OF_HEARTS, RED_FOUR_OF_HEARTS, RED_FIVE_OF_HEARTS, RED_SIX_OF_HEARTS,
                  RED_SEVEN_OF_HEARTS, RED_EIGHT_OF_HEARTS, RED_NINE_OF_HEARTS, RED_TEN_OF_HEARTS, RED_JACK_OF_HEARTS, RED_KING_OF_HEARTS,
                  RED_QUEEN_OF_HEARTS, RED_ACE_OF_DIAMONDS, RED_TWO_OF_DIAMONDS, RED_THREE_OF_DIAMONDS, RED_FOUR_OF_DIAMONDS, RED_FIVE_OF_DIAMONDS,
                  RED_SIX_OF_DIAMONDS, RED_SEVEN_OF_DIAMONDS, RED_EIGHT_OF_DIAMONDS, RED_NINE_OF_DIAMONDS, RED_TEN_OF_DIAMONDS, RED_JACK_OF_DIAMONDS,
                  RED_KING_OF_DIAMONDS, RED_QUEEN_OF_DIAMONDS, RED_ACE_OF_CLUBS, RED_TWO_OF_CLUBS, RED_THREE_OF_CLUBS, RED_FOUR_OF_CLUBS,
                  RED_FIVE_OF_CLUBS, RED_SIX_OF_CLUBS, RED_SEVEN_OF_CLUBS, RED_EIGHT_OF_CLUBS, RED_NINE_OF_CLUBS, RED_TEN_OF_CLUBS,
                  RED_JACK_OF_CLUBS, RED_KING_OF_CLUBS, RED_QUEEN_OF_CLUBS, RED_ACE_OF_SPADES, RED_TWO_OF_SPADES, RED_THREE_OF_SPADES,
                  RED_FOUR_OF_SPADES, RED_FIVE_OF_SPADES, RED_SIX_OF_SPADES, RED_SEVEN_OF_SPADES, RED_EIGHT_OF_SPADES, RED_NINE_OF_SPADES,
                  RED_TEN_OF_SPADES, RED_JACK_OF_SPADES, RED_KING_OF_SPADES, RED_QUEEN_OF_SPADES, RED_BLACK_JOKER, RED_RED_JOKER]
random.shuffle(RED_DRAW_DECK)
DISCARD_PILE = []
# endregion


def draw_window():
    if Meta.CURRENT_STATE == ScreenState.START:  # Start Menu
        WINDOW.fill(BLUE)
        draw_text("Tyche's Game", BIG_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 960, 300, 60)
        if quit_button.check_click():
            pygame.quit()
        new_game_button = Button("New Game", 960, 200, 60)
        if new_game_button.check_click():
            Meta.CURRENT_STATE = ScreenState.NEW_MENU
    elif Meta.CURRENT_STATE == ScreenState.NEW_MENU:  # New Game Menu
        WINDOW.fill((100, 100, 100))
        draw_text("How many players?", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 960, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        back_button = Button("Back", 800, 600, 60)
        if back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.START
        two_player_button = Button("Two Players", 300, 200, 60, BLUE, ORANGE, SMALL_FONT, 220)
        three_player_button = Button("Three Players", 700, 200, 60, BLUE, ORANGE, SMALL_FONT, 220)
        four_player_button = Button("Four Players", 300, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        five_player_button = Button("Five Players", 700, 300, 60, BLUE, ORANGE, SMALL_FONT, 220)
        if two_player_button.check_click():
            Meta.PLAYER_COUNT = 2
        elif three_player_button.check_click():
            Meta.PLAYER_COUNT = 3
        elif four_player_button.check_click():
            Meta.PLAYER_COUNT = 4
        elif five_player_button.check_click():
            Meta.PLAYER_COUNT = 5
        if Meta.PLAYER_COUNT is not None:
            Meta.CAN_TEXT_INPUT = True
            Meta.CURRENT_STATE = ScreenState.PLAYER_NAMING
    elif Meta.CURRENT_STATE == ScreenState.PLAYER_NAMING:  # Player Naming Menu
        WINDOW.fill(BLACK)
        quit_button = Button("Quit", 960, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        elif Meta.CURRENT_PLAYER == Meta.PLAYER_COUNT:
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_ONE
            Meta.CURRENT_PLAYER = 0
            random.shuffle(Meta.PLAYERS)
        else:
            match Meta.CURRENT_PLAYER:  # Draw Screen Title
                case 0:
                    draw_text("Enter Player One's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 1:
                    draw_text("Enter Player Two's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 2:
                    draw_text("Enter Player Three's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 3:
                    draw_text("Enter Player Four's Name", MEDIUM_FONT, ORANGE, (960, 69))
                case 4:
                    draw_text("Enter Player Five's Name", MEDIUM_FONT, ORANGE, (960, 69))
            draw_text_input()
            if Meta.TEXT_CONFIRMED:
                Meta.PLAYERS.append(Player(Meta.CURRENT_PLAYER, Meta.USER_TEXT))
                Meta.USER_TEXT = ""
                Meta.CURRENT_PLAYER += 1
                Meta.TEXT_CONFIRMED = False
    elif Meta.CURRENT_STATE == ScreenState.GAME_INTRO_ONE:
        WINDOW.fill((30, 100, 150))
        quit_button = Button("Quit", 200, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        draw_text("Welcome to Tyche's Game", BIG_FONT, ORANGE, (960, 69))
        page_background = pygame.Rect((460, 150), (1000, 850))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, page_background, 0, 5)
        draw_text("Scenario", MEDIUM_FONT, ORANGE, (960, 190))
        draw_text("Tyche, the Goddess of Chance, has had enough of humanity", SMALL_FONT, BLACK, (960, 250))
        draw_text("blaming Luck for their own errors, so she has decided to", SMALL_FONT, BLACK, (960, 290))
        draw_text("entrap some humans in her game to show them what Luck", SMALL_FONT, BLACK, (960, 330))
        draw_text("truly means.", SMALL_FONT, BLACK, (960, 370))
        draw_text("However, Tyche's game isn't all about Luck and Chance. There's", SMALL_FONT, BLACK, (960, 490))
        draw_text("also a degree of human skill involved in the process. This skill", SMALL_FONT, BLACK, (960, 530))
        draw_text("comes in several different forms, which you will learn of in time.", SMALL_FONT, BLACK, (960, 570))
        draw_text("You find yourselves in a dark room containing just an empty table.", SMALL_FONT, BLACK, (960, 690))
        next_button = Button(">", 1420, 760, 70, WHITE, BLACK, MEDIUM_FONT)
        if next_button.check_click() or Meta.RIGHT_ARROW_DOWN:
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
    elif Meta.CURRENT_STATE == ScreenState.GAME_INTRO_TWO:
        WINDOW.fill((30, 100, 150))
        quit_button = Button("Quit", 200, 600, 60)
        if quit_button.check_click():
            pygame.quit()
        draw_text("Welcome to Tyche's Game", BIG_FONT, ORANGE, (960, 69))
        page_background = pygame.Rect((460, 150), (1000, 850))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, page_background, 0, 5)
        draw_text("Understanding the Game", MEDIUM_FONT, ORANGE, (960, 190))
        draw_text("Tyche's game is visually similar to Snakes & Ladders with", SMALL_FONT, BLACK, (960, 250))
        draw_text("the fact that you need to ascend the board to win. However,", SMALL_FONT, BLACK, (960, 290))
        draw_text("there are also two decks of playing cards that are in play. These", SMALL_FONT, BLACK, (960, 330))
        draw_text("change the way the game is played somewhat with the Blue being", SMALL_FONT, BLACK, (960, 370))
        draw_text("positive and the Red being negative. You can click below to see", SMALL_FONT, BLACK, (960, 410))
        draw_text("the effect each card has on the game.", SMALL_FONT, BLACK, (960, 450))
        draw_text("The board will contain symbols that determine what type of space", SMALL_FONT, BLACK, (960, 570))
        draw_text("you'd be in. There is a guide below to help you understand it.", SMALL_FONT, BLACK, (960, 610))
        back_button = Button("<", 500, 760, 70, WHITE, BLACK, MEDIUM_FONT)
        blue_guide_button = Button("Blue Card Guide", 800, 690, 60, WHITE, BLACK, SMALL_FONT)
        red_guide_button = Button("Red Card Guide", 1120, 690, 60, WHITE, BLACK, SMALL_FONT)
        board_guide_button = Button("Board Symbols Guide", 950, 790, 60, WHITE, BLACK, SMALL_FONT)
        play_game_button = Button("Play Game", 1360, 760, 60, WHITE, BLACK, SMALL_FONT)
        if back_button.check_click() or Meta.LEFT_ARROW_DOWN:
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_ONE
        elif blue_guide_button.check_click():
            Meta.CURRENT_STATE = ScreenState.BLUE_CARD_GUIDE
        elif red_guide_button.check_click():
            Meta.CURRENT_STATE = ScreenState.RED_CARD_GUIDE
        elif board_guide_button.check_click():
            Meta.CURRENT_STATE = ScreenState.BOARD_SYMBOLS_GUIDE
        elif play_game_button.check_click():
            Meta.CURRENT_STATE = ScreenState.PLAYING_GAME
            D6.enabled = True
            for x in range(len(Meta.PLAYERS)):
                BOARD_SQUARES[0].players.append(Meta.PLAYERS[x])
    elif Meta.CURRENT_STATE == ScreenState.BLUE_CARD_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Blue Card Guide", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 1280, 950, 60)
        back_button = Button("Back", 640, 950, 60)
        if quit_button.check_click():
            pygame.quit()
        elif back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_card(BLUE_ACE_OF_HEARTS, (320, 270), 2)
        draw_card(BLUE_TWO_OF_HEARTS, (640, 270), 2)
        draw_card(BLUE_THREE_OF_HEARTS, (960, 270), 2)
        draw_card(BLUE_FOUR_OF_HEARTS, (1280, 270), 2)
        draw_card(BLUE_FIVE_OF_HEARTS, (1600, 270), 2)
        draw_card(BLUE_SIX_OF_HEARTS, (320, 540), 2)
        draw_card(BLUE_SEVEN_OF_HEARTS, (640, 540), 2)
        draw_card(BLUE_EIGHT_OF_HEARTS, (960, 540), 2)
        draw_card(BLUE_NINE_OF_HEARTS, (1280, 540), 2)
        draw_card(BLUE_TEN_OF_HEARTS, (1600, 540), 2)
        draw_card(BLUE_JACK_OF_HEARTS, (320, 810), 2)
        draw_card(BLUE_KING_OF_HEARTS, (640, 810), 2)
        draw_card(BLUE_QUEEN_OF_HEARTS, (960, 810), 2)
        draw_card(BLUE_RED_JOKER, (1280, 810), 2)
        draw_card(BLUE_BLACK_JOKER, (1600, 810), 2)
        check_hover_boxes()
    elif Meta.CURRENT_STATE == ScreenState.RED_CARD_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Red Card Guide", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 1280, 950, 60)
        back_button = Button("Back", 640, 950, 60)
        if quit_button.check_click():
            pygame.quit()
        elif back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_card(RED_ACE_OF_HEARTS, (320, 270), 2)
        draw_card(RED_TWO_OF_HEARTS, (640, 270), 2)
        draw_card(RED_THREE_OF_HEARTS, (960, 270), 2)
        draw_card(RED_FOUR_OF_HEARTS, (1280, 270), 2)
        draw_card(RED_FIVE_OF_HEARTS, (1600, 270), 2)
        draw_card(RED_SIX_OF_HEARTS, (320, 540), 2)
        draw_card(RED_SEVEN_OF_HEARTS, (640, 540), 2)
        draw_card(RED_EIGHT_OF_HEARTS, (960, 540), 2)
        draw_card(RED_NINE_OF_HEARTS, (1280, 540), 2)
        draw_card(RED_TEN_OF_HEARTS, (1600, 540), 2)
        draw_card(RED_JACK_OF_HEARTS, (320, 810), 2)
        draw_card(RED_KING_OF_HEARTS, (640, 810), 2)
        draw_card(RED_QUEEN_OF_HEARTS, (960, 810), 2)
        draw_card(RED_RED_JOKER, (1280, 810), 2)
        draw_card(RED_BLACK_JOKER, (1600, 810), 2)
        check_hover_boxes()
    elif Meta.CURRENT_STATE == ScreenState.BOARD_SYMBOLS_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Board Symbols Guide", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 960, 900, 60)
        back_button = Button("Back", 960, 800, 60)
        if quit_button.check_click():
            pygame.quit()
        elif back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_game_image(BLUE_CARD_SYMBOL, (320, 270), 2, True, WHITE, (330, 80),
                        "Blue Card", "", "Draw 1 from the Blue Draw Deck")
        draw_game_image(RED_CARD_SYMBOL, (640, 270), 2, True, WHITE, (330, 80),
                        "Red Card", "", "Draw 1 from the Red Draw Deck")
        draw_game_image((MISS_TURN, (89, 89)), (960, 270), 2, True, WHITE, (330, 80),
                        "Miss a Turn", "", "Landing here traps you for a turn")
        check_hover_boxes()
    elif Meta.CURRENT_STATE == ScreenState.PLAYING_GAME:
        WINDOW.fill(WHITE)
        Meta.BUTTONS_ENABLED = True
        current_player = Meta.PLAYERS[Meta.CURRENT_PLAYER]
        draw_text(current_player.playerName + "'s Turn", SMALL_FONT, PLAYER_TO_COLOUR[current_player.playerNumber], (960, 30))
        game_board = pygame.Rect((480, 60), (960, 960))
        pygame.draw.rect(WINDOW, BLUE, game_board)
        roll_background = pygame.Rect((1460, 100), (440, 700))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, roll_background, 0, 20)
        draw_game_image(BLUE_CARD_SYMBOL, (360, 250), 3, True, PASTEL_GREEN, (170, 75),
                        "Blue Draw Pile", "", "Current Size: " + str(len(BLUE_DRAW_DECK)))
        draw_game_image(RED_CARD_SYMBOL, (360, 650), 3, True, PASTEL_GREEN, (170, 75),
                        "Red Draw Pile", "", "Current Size: " + str(len(RED_DRAW_DECK)))
        if len(current_player.blueDeck) != 0:
            turned_blue_deck_image = pygame.transform.rotate(BLUE_CARD_SYMBOL[0], -90)
            turned_blue_deck_image = pygame.transform.scale(turned_blue_deck_image, (BLUE_CARD_SYMBOL[1][1] * 3, BLUE_CARD_SYMBOL[1][0] * 3))
            WINDOW.blit(turned_blue_deck_image, (95, 835))
            if Meta.CARD_HANDS_ACTIVE: Meta.HOVER_BOXES.append(("board symbol", ["Your Blue Card Hand"], turned_blue_deck_image, (95, 835), (215, 35), PASTEL_GREEN))
            blue_hand_rect = turned_blue_deck_image.get_rect()
            blue_hand_rect.topleft = (95, 835)
            if blue_hand_rect.collidepoint(pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED and Meta.CARD_HANDS_ACTIVE:
                Meta.SHOW_HAND = CardType.BLUE
                Meta.CARD_HANDS_ACTIVE = False
                if Meta.CARDS_TO_DRAW is not None:
                    Meta.CARDS_TO_DRAW = max(Meta.CARDS_TO_DRAW - 1, 0)
                Meta.DISPLAY_CARD = None
        if len(current_player.redDeck) != 0:
            turned_red_deck_image = pygame.transform.rotate(RED_CARD_SYMBOL[0], 90)
            turned_red_deck_image = pygame.transform.scale(turned_red_deck_image, (RED_CARD_SYMBOL[1][1] * 3, RED_CARD_SYMBOL[1][0] * 3))
            WINDOW.blit(turned_red_deck_image, (1530, 835))
            if Meta.CARD_HANDS_ACTIVE: Meta.HOVER_BOXES.append(("board symbol", ["Your Red Card Hand"], turned_red_deck_image, (1530, 835), (215, 35), PASTEL_GREEN))
            red_hand_rect = turned_red_deck_image.get_rect()
            red_hand_rect.topleft = (1530, 835)
            if red_hand_rect.collidepoint(pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED and Meta.CARD_HANDS_ACTIVE:
                Meta.SHOW_HAND = CardType.RED
                Meta.CARD_HANDS_ACTIVE = False
                if Meta.CARDS_TO_DRAW is not None:
                    Meta.CARDS_TO_DRAW = max(Meta.CARDS_TO_DRAW - 1, 0)
                Meta.DISPLAY_CARD = None
        for x in range(len(BOARD_SQUARES)):  # Draw Squares
            square = BOARD_SQUARES[x]
            square_rect = pygame.Rect((square.center[0] - 44, square.center[1] - 44), (89, 89))
            pygame.draw.rect(WINDOW, WHITE, square_rect)
            if x == 0:  # Start Square
                draw_text("START", TINY_FONT, BLUE, square.center)
            elif x == 99:  # Finish Square
                draw_text("FINISH", TINY_FONT, BLUE, square.center)
            else:
                draw_text(str(x + 1), TINY_FONT, BLUE, (square.center[0] - 30, square.center[1] + 35))
                if square.symbol is not None: draw_game_image((square.symbol, (89, 89)), square.center, 1)
            for i in range(len(square.players)):
                player_image = square.players[i].playerPiece
                WINDOW.blit(player_image, ((square.center[0] + PLAYER_TO_POSITION[i][0]) - 14, (square.center[1] + PLAYER_TO_POSITION[i][1]) - 14))
        if Meta.SHOW_HAND is None: check_hover_boxes()
        if Meta.SHOW_HAND == CardType.BLUE:
            Meta.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text(current_player.playerName + "'s Blue Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
            back_button = Button("Back", 960, 950, 60)
            if back_button.check_click():
                Meta.SHOW_HAND = None
                Meta.CARD_HANDS_ACTIVE = True
            for x in range(len(current_player.blueDeck)):
                draw_card(current_player.blueDeck[x], CARD_TO_POSITION[x], 2)
            Meta.BUTTONS_ENABLED = False
            check_hover_boxes()
        elif Meta.SHOW_HAND == CardType.RED:
            Meta.HOVER_BOXES.clear()
            WINDOW.fill(PASTEL_GREEN)
            draw_text(current_player.playerName + "'s Red Card Hand", MEDIUM_FONT, ORANGE, (960, 69))
            back_button = Button("Back", 960, 950, 60)
            if back_button.check_click():
                Meta.SHOW_HAND = None
                Meta.CARD_HANDS_ACTIVE = True
            for x in range(len(current_player.redDeck)):
                draw_card(current_player.redDeck[x], CARD_TO_POSITION[x], 2)
            Meta.BUTTONS_ENABLED = False
            check_hover_boxes()
        elif Meta.TURN_STAGE == TurnStage.ROLL_DICE:  # Rolling the Movement Dice
            if current_player.missNextTurn:
                draw_text("You don't get to take this turn", SMALL_FONT, BLACK, (1680, 240))
                continue_button = Button("Continue", 1680, 600, 60)
                if continue_button.check_click():
                    current_player.missNextTurn = False
                    if Meta.CURRENT_PLAYER == Meta.PLAYER_COUNT - 1:
                        Meta.CURRENT_PLAYER = 0
                    else:
                        Meta.CURRENT_PLAYER += 1
                    D6.enabled = True
            else:
                draw_text("Roll the d6 to move:", SMALL_FONT, BLACK, (1680, 240))
                draw_dice(D6, (1680, 330), 2)
                if D6.check_click():
                    Meta.TURN_STAGE = TurnStage.MOVEMENT
        elif Meta.TURN_STAGE == TurnStage.MOVEMENT:  # Moving the Current Player
            draw_dice(D6, (1680, 330), 2)
            BOARD_SQUARES[current_player.currentSquare].players.remove(current_player)
            current_player.currentSquare = min(99, current_player.currentSquare + D6.sideFacing)
            BOARD_SQUARES[current_player.currentSquare].players.append(current_player)
            Meta.TURN_STAGE = TurnStage.SQUARE_ACTION
            Meta.CAN_PROGRESS = False
        elif Meta.TURN_STAGE == TurnStage.SQUARE_ACTION:  # Doing what the Square wants
            draw_dice(D6, (1680, 330), 2)
            current_square = BOARD_SQUARES[current_player.currentSquare]
            if current_player.currentSquare == 99:
                Meta.TURN_STAGE = TurnStage.GAME_WON
            else:
                if Meta.DISPLAY_CARD == CardType.BLUE:
                    draw_card(current_player.blueDeck[len(current_player.blueDeck) - 1], (1680, 380), 3)
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        # On Draw Card Actions
                        Meta.CARDS_TO_DRAW -= 1
                        Meta.DISPLAY_CARD = None
                    check_hover_boxes()
                elif Meta.DISPLAY_CARD == CardType.RED:
                    draw_card(current_player.redDeck[len(current_player.redDeck) - 1], (1680, 380), 3)
                    continue_button = Button("Continue", 1680, 600, 60)
                    if continue_button.check_click():
                        # On Draw Card Actions
                        Meta.CARDS_TO_DRAW -= 1
                        Meta.DISPLAY_CARD = None
                    check_hover_boxes()
                else:
                    if current_square.symbol == ONE_BLUE:
                        draw_text("Draw One Blue Card", SMALL_FONT, BLACK, (1680, 240))
                        if Meta.CARDS_TO_DRAW is None:
                            Meta.CARDS_TO_DRAW = 1
                        if Meta.CARDS_TO_DRAW == 0:
                            Meta.CAN_PROGRESS = True
                            Meta.CARDS_TO_DRAW = None
                        else:
                            check_get_card(CardType.BLUE)
                    elif current_square.symbol == ONE_RED:
                        draw_text("Draw One Red Card", SMALL_FONT, BLACK, (1680, 240))
                        if Meta.CARDS_TO_DRAW is None:
                            Meta.CARDS_TO_DRAW = 1
                        if Meta.CARDS_TO_DRAW == 0:
                            Meta.CAN_PROGRESS = True
                            Meta.CARDS_TO_DRAW = None
                        else:
                            check_get_card(CardType.RED)
                    elif current_square.symbol == MISS_TURN:
                        draw_text("You Miss your Next Turn", SMALL_FONT, BLACK, (1680, 240))
                        current_player.missNextTurn = True
                        continue_button = Button("Continue", 1680, 600, 60)
                        if continue_button.check_click():
                            Meta.CAN_PROGRESS = True
                    elif current_square.symbol is None:
                        Meta.CAN_PROGRESS = True
                    if Meta.CAN_PROGRESS:
                        Meta.TURN_STAGE = TurnStage.END_TURN
        elif Meta.TURN_STAGE == TurnStage.END_TURN:
            draw_dice(D6, (1680, 330), 2)
            continue_button = Button("Continue", 1680, 600, 60)
            if continue_button.check_click():
                Meta.TURN_STAGE = TurnStage.ROLL_DICE
                if Meta.CURRENT_PLAYER == Meta.PLAYER_COUNT - 1:
                    Meta.CURRENT_PLAYER = 0
                else:
                    Meta.CURRENT_PLAYER += 1
                D6.enabled = True
        elif Meta.TURN_STAGE == TurnStage.GAME_WON:
            draw_text(current_player.playerName + " has Won!!", SMALL_FONT, BLACK, (1680, 240))
        if Meta.SHOW_HAND is None:
            quit_button = Button("Quit", 360, 450, 60)
            if quit_button.check_click():
                pygame.quit()


def draw_text(text, font, colour, location, center = True):  # Draws text centered on a location
    text_surface = font.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    if center:
        WINDOW.blit(text_surface, (location[0] - (text_width/2), location[1] - (text_height/2)))
    else:
        WINDOW.blit(text_surface, location)


def draw_text_input(location = (960, 400), max_length = 300):  # Creates Text Input Visuals
    text_surface = SMALL_FONT.render(Meta.USER_TEXT, True, ORANGE)
    if text_surface.get_width() >= max_length:
        Meta.CAN_TEXT_INPUT = False
    else:
        Meta.CAN_TEXT_INPUT = True
    input_rect_width = max(text_surface.get_width() + 10, 200)
    input_rect = pygame.Rect(location[0] - (input_rect_width / 2), location[1], input_rect_width, 60)
    pygame.draw.rect(WINDOW, BLUE, input_rect, 2)
    WINDOW.blit(text_surface, ((input_rect.x + (input_rect.width / 2)) - (text_surface.get_width() / 2), (input_rect.y + (input_rect.height / 2)) -
    text_surface.get_height() / 2))


def draw_card(card, location, scale, hover_box = True):
    card_image = pygame.image.load(card.imagePath)
    card_width = CARD_SIZE[0] * scale
    card_height = CARD_SIZE[1] * scale
    card_image = pygame.transform.scale(card_image, (card_width, card_height))
    new_location = (location[0] - (card_width/2), location[1] - (card_height/2))
    if hover_box:
        card_usable = False
        if Meta.SHOW_HAND is not None and check_card_usable(card):
            card_usable = True
            card_rect = card_image.get_rect()
            card_rect.topleft = new_location
            if card_rect.collidepoint(pygame.mouse.get_pos()) and Meta.LEFT_MOUSE_RELEASED:
                perform_card_action(card)
        Meta.HOVER_BOXES.append(("card", card, card_image, new_location, card_usable))
    WINDOW.blit(card_image, new_location)


def draw_dice(dice, location, scale):
    dice_width = dice.valueToImage[dice.sideFacing][1][0] * scale
    dice_height = dice.valueToImage[dice.sideFacing][1][1] * scale
    dice_image = dice.valueToImage[dice.sideFacing][0]
    dice_image = pygame.transform.scale(dice_image, (dice_width, dice_height))
    new_location = (location[0] - (dice_width/2), location[1] - (dice_height/2))
    dice.currentRect = pygame.Rect(new_location, (dice_width, dice_height))
    WINDOW.blit(dice_image, new_location)


def draw_game_image(symbol, location, scale, hover_box = False, colour = WHITE, desc_size = (0, 0), *desc_lines):
    image_width = symbol[1][0] * scale
    image_height = symbol[1][1] * scale
    image = symbol[0]
    image = pygame.transform.scale(image, (image_width, image_height))
    new_location = (location[0] - (image_width/2), location[1] - (image_height/2))
    if hover_box:
        Meta.HOVER_BOXES.append(("board symbol", desc_lines, image, new_location, desc_size, colour))
    WINDOW.blit(image, new_location)


def check_get_card(card_colour):
    mouse_pos = pygame.mouse.get_pos()
    if card_colour == CardType.BLUE:
        if BLUE_DRAW_DECK_RECT.collidepoint(mouse_pos) and Meta.LEFT_MOUSE_RELEASED:
            card = BLUE_DRAW_DECK.pop()
            Meta.PLAYERS[Meta.CURRENT_PLAYER].blueDeck.append(card)
            Meta.DISPLAY_CARD = CardType.BLUE
            return True
    else:
        if RED_DRAW_DECK_RECT.collidepoint(mouse_pos) and Meta.LEFT_MOUSE_RELEASED:
            card = RED_DRAW_DECK.pop()
            Meta.PLAYERS[Meta.CURRENT_PLAYER].redDeck.append(card)
            Meta.DISPLAY_CARD = CardType.RED
            return True
    return False


def check_card_usable(card):
    if card.cardType == CardType.BLUE:
        match card.cardValue:
            case CardValue.ACE:  # True if there is a non-Joker Card in the Discard Pile
                for card in DISCARD_PILE:
                    if card.cardValue != CardValue.JOKER:
                        return True
            case CardValue.TWO:  # True anytime you need to roll a dice
                if Meta.TURN_STAGE == TurnStage.ROLL_DICE:
                    return True
            case CardValue.THREE:  # Always True
                return True
            case CardValue.FOUR:  # True anytime you are about to roll for damage
                return True
            case CardValue.FIVE:  # Always True
                return True
            case CardValue.SIX:
                return True
            case CardValue.SEVEN:
                return True
            case CardValue.EIGHT:  # True after losing a defence roll
                return True
            case CardValue.NINE:  # Always True
                return True
            case CardValue.TEN:  # Never True (Card Uses Automatically)
                return False
            case CardValue.JACK:  # True anytime you are about to roll for movement
                if Meta.TURN_STAGE == TurnStage.ROLL_DICE:
                    return True
            case CardValue.KING:
                return True
            case CardValue.QUEEN:  # True anytime you need to draw Red Cards
                return True
            case CardValue.JOKER:
                return True
    else:
        match card.cardValue:
            case CardValue.ACE:
                return True
            case CardValue.TWO:
                return True
            case CardValue.THREE:
                return True
            case CardValue.FOUR:
                return True
            case CardValue.FIVE:
                return True
            case CardValue.SIX:
                return True
            case CardValue.SEVEN:
                return True
            case CardValue.EIGHT:
                return True
            case CardValue.NINE:
                return True
            case CardValue.TEN:
                return True
            case CardValue.JACK:
                return True
            case CardValue.KING:
                return True
            case CardValue.QUEEN:
                return True
            case CardValue.JOKER:
                return True
    return False


def perform_card_action(card):
    if card.cardType == CardType.BLUE:
        match card.cardValue:
            case CardValue.ACE:
                print("Card Used: " + card.displayName)
            case CardValue.TWO:
                print("Card Used: " + card.displayName)
            case CardValue.THREE:
                print("Card Used: " + card.displayName)
            case CardValue.FOUR:
                print("Card Used: " + card.displayName)
            case CardValue.FIVE:
                print("Card Used: " + card.displayName)
            case CardValue.SIX:
                print("Card Used: " + card.displayName)
            case CardValue.SEVEN:
                print("Card Used: " + card.displayName)
            case CardValue.EIGHT:
                print("Card Used: " + card.displayName)
            case CardValue.NINE:
                print("Card Used: " + card.displayName)
            case CardValue.TEN:
                print("Card Used: " + card.displayName)
            case CardValue.JACK:
                print("Card Used: " + card.displayName)
            case CardValue.KING:
                print("Card Used: " + card.displayName)
            case CardValue.QUEEN:
                print("Card Used: " + card.displayName)
            case CardValue.JOKER:
                print("Card Used: " + card.displayName)
        Meta.CARD_TO_REMOVE = (Meta.PLAYERS[Meta.CURRENT_PLAYER].blueDeck, card)
    else:
        match card.cardValue:
            case CardValue.ACE:
                print("Card Used: " + card.displayName)
            case CardValue.TWO:
                print("Card Used: " + card.displayName)
            case CardValue.THREE:
                print("Card Used: " + card.displayName)
            case CardValue.FOUR:
                print("Card Used: " + card.displayName)
            case CardValue.FIVE:
                print("Card Used: " + card.displayName)
            case CardValue.SIX:
                print("Card Used: " + card.displayName)
            case CardValue.SEVEN:
                print("Card Used: " + card.displayName)
            case CardValue.EIGHT:
                print("Card Used: " + card.displayName)
            case CardValue.NINE:
                print("Card Used: " + card.displayName)
            case CardValue.TEN:
                print("Card Used: " + card.displayName)
            case CardValue.JACK:
                print("Card Used: " + card.displayName)
            case CardValue.KING:
                print("Card Used: " + card.displayName)
            case CardValue.QUEEN:
                print("Card Used: " + card.displayName)
            case CardValue.JOKER:
                print("Card Used: " + card.displayName)
        Meta.CARD_TO_REMOVE = (Meta.PLAYERS[Meta.CURRENT_PLAYER].redDeck, card)
    DISCARD_PILE.append(card)
    Meta.SHOW_HAND = None
    Meta.CARD_HANDS_ACTIVE = True


def check_hover_boxes():
    for hover_box in Meta.HOVER_BOXES:
        if hover_box[0] == "card":
            card_rect = hover_box[2].get_rect()
            card_rect.topleft = hover_box[3]
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                rect_size = hover_box[1].descRectSize
                desc_lines = hover_box[1].descLines
                if Meta.SHOW_HAND is not None:
                    if hover_box[4]:
                        rect_size = (hover_box[1].descRectSize[0], hover_box[1].descRectSize[1] + 35)
                        desc_lines = desc_lines + ("", "Click to Use Card")
                if mouse_pos[0] <= 960:  # Card Desc. Horizontal Positioning
                    rect_left_position = mouse_pos[0] + 5
                else:
                    rect_left_position = mouse_pos[0] - rect_size[0]
                if mouse_pos[1] <= 540:
                    rect_top_position = mouse_pos[1] + 5
                else:
                    rect_top_position = mouse_pos[1] - rect_size[1]
                # Draw Card Name and Description
                card_desc_rect = pygame.Rect((rect_left_position, rect_top_position), rect_size)
                pygame.draw.rect(WINDOW, WHITE, card_desc_rect, 0, 5)
                draw_text(hover_box[1].displayName, TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + 5), False)
                for x in range(len(desc_lines)):
                    draw_text(desc_lines[x], TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + (20 * (x + 2))), False)
        elif hover_box[0] == "board symbol":
            card_rect = hover_box[2].get_rect()
            card_rect.topleft = hover_box[3]
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                if mouse_pos[0] <= 960:  # Card Back Desc. Horizontal Positioning
                    rect_left_position = mouse_pos[0] + 5
                else:
                    rect_left_position = mouse_pos[0] - hover_box[4][0]
                if mouse_pos[1] <= 540:
                    rect_top_position = mouse_pos[1] + 5
                else:
                    rect_top_position = mouse_pos[1] - hover_box[4][1]
                card_desc_rect = pygame.Rect((rect_left_position, rect_top_position), hover_box[4])
                pygame.draw.rect(WINDOW, hover_box[5], card_desc_rect, 0, 5)
                for x in range(len(hover_box[1])):
                    draw_text(hover_box[1][x], TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + ((20 * x) + 5)), False)


def display_debug_info():
    if DEBUG_MODE:
        for x in range(len(Meta.DEBUG_INFO)):
            draw_text(Meta.DEBUG_INFO[x][0], TINY_FONT, Meta.DEBUG_INFO[x][1], (10, 10 + (20 * x)), False)


def main():  # Game Loop
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        Meta.HOVER_BOXES.clear()
        Meta.DEBUG_INFO.clear()
        if Meta.CURRENT_STATE == ScreenState.PLAYING_GAME:
            Meta.DEBUG_INFO.append((str(Meta.TURN_STAGE), BLACK))
            Meta.DEBUG_INFO.append(("Discard Pile Size: " + str(len(DISCARD_PILE)), BLACK))
            Meta.DEBUG_INFO.append(("Player Turn Order:", BLACK))
            for player in Meta.PLAYERS:
                text = player.playerName
                if player == Meta.PLAYERS[Meta.CURRENT_PLAYER]:
                    text += " -"
                Meta.DEBUG_INFO.append((text, player.playerColour))
        # Game Events
        Meta.LEFT_MOUSE_RELEASED = False
        Meta.LEFT_ARROW_DOWN = False
        Meta.RIGHT_ARROW_DOWN = False
        for event in pygame.event.get():  # Event Handler
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Meta.LEFT_MOUSE_RELEASED = True
            elif event.type == BUTTON_COOLDOWN_EVENT:
                Meta.BUTTONS_ENABLED = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Meta.LEFT_ARROW_DOWN = True
                elif event.key == pygame.K_RIGHT:
                    Meta.RIGHT_ARROW_DOWN = True
                if event.key in ALLOWED_KEYS:
                    if event.key == pygame.K_BACKSPACE:
                        Meta.USER_TEXT = Meta.USER_TEXT[:-1]
                    elif event.key == pygame.K_RETURN:
                        Meta.TEXT_CONFIRMED = True
                    elif Meta.CAN_TEXT_INPUT:
                        Meta.USER_TEXT += event.unicode
        draw_window()
        display_debug_info()
        pygame.display.update()
        if Meta.CARD_TO_REMOVE is not None:
            Meta.CARD_TO_REMOVE[0].remove(Meta.CARD_TO_REMOVE[1])
            Meta.CARD_TO_REMOVE = None


if __name__ == "__main__":
    main()
