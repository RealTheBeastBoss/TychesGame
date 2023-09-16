import random

import pygame.draw

from card import *
from meta import *
from button import Button
from player import Player


pygame.display.set_caption("Tyche's Game")

# Game Cards
# region
BLUE_ACE_OF_HEARTS = Card("Blue Ace of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.ACE, "ace_hearts.png", (300, 150),
                          "This is a test card description", "with two lines")
BLUE_TWO_OF_HEARTS = Card("Blue Two of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.TWO, "2_hearts.png")
BLUE_THREE_OF_HEARTS = Card("Blue Three of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.THREE, "3_hearts.png")
BLUE_FOUR_OF_HEARTS = Card("Blue Four of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.FOUR, "4_hearts.png")
BLUE_FIVE_OF_HEARTS = Card("Blue Five of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.FIVE, "5_hearts.png")
BLUE_SIX_OF_HEARTS = Card("Blue Six of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.SIX, "6_hearts.png")
BLUE_SEVEN_OF_HEARTS = Card("Blue Seven of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.SEVEN, "7_hearts.png")
BLUE_EIGHT_OF_HEARTS = Card("Blue Eight of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.EIGHT, "8_hearts.png", (300, 150))
BLUE_NINE_OF_HEARTS = Card("Blue Nine of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.NINE, "9_hearts.png")
BLUE_TEN_OF_HEARTS = Card("Blue Ten of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.TEN, "10_hearts.png")
BLUE_JACK_OF_HEARTS = Card("Blue Jack of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.JACK, "jack_hearts.png")
BLUE_KING_OF_HEARTS = Card("Blue King of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.KING, "king_hearts.png")
BLUE_QUEEN_OF_HEARTS = Card("Blue Queen of Hearts", CardType.BLUE, CardSuit.HEARTS, CardValue.QUEEN, "queen_hearts.png")
BLUE_ACE_OF_DIAMONDS = Card("Blue Ace of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.ACE, "ace_diamonds.png")
BLUE_TWO_OF_DIAMONDS = Card("Blue Two of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.TWO, "2_diamonds.png")
BLUE_THREE_OF_DIAMONDS = Card("Blue Three of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.THREE, "3_diamonds.png")
BLUE_FOUR_OF_DIAMONDS = Card("Blue Four of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.FOUR, "4_diamonds.png")
BLUE_FIVE_OF_DIAMONDS = Card("Blue Five of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.FIVE, "5_diamonds.png")
BLUE_SIX_OF_DIAMONDS = Card("Blue Six of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.SIX, "6_diamonds.png")
BLUE_SEVEN_OF_DIAMONDS = Card("Blue Seven of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.SEVEN, "7_diamonds.png")
BLUE_EIGHT_OF_DIAMONDS = Card("Blue Eight of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.EIGHT, "8_diamonds.png")
BLUE_NINE_OF_DIAMONDS = Card("Blue Nine of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.NINE, "9_diamonds.png")
BLUE_TEN_OF_DIAMONDS = Card("Blue Ten of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.TEN, "10_diamonds.png")
BLUE_JACK_OF_DIAMONDS = Card("Blue Jack of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.JACK, "jack_diamonds.png")
BLUE_KING_OF_DIAMONDS = Card("Blue King of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.KING, "king_diamonds.png")
BLUE_QUEEN_OF_DIAMONDS = Card("Blue Queen of Diamonds", CardType.BLUE, CardSuit.DIAMONDS, CardValue.QUEEN, "queen_diamonds.png")
BLUE_ACE_OF_CLUBS = Card("Blue Ace of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.ACE, "ace_clubs.png")
BLUE_TWO_OF_CLUBS = Card("Blue Two of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.TWO, "2_clubs.png")
BLUE_THREE_OF_CLUBS = Card("Blue Three of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.THREE, "3_clubs.png")
BLUE_FOUR_OF_CLUBS = Card("Blue Four of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.FOUR, "4_clubs.png")
BLUE_FIVE_OF_CLUBS = Card("Blue Five of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.FIVE, "5_clubs.png")
BLUE_SIX_OF_CLUBS = Card("Blue Six of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.SIX, "6_clubs.png")
BLUE_SEVEN_OF_CLUBS = Card("Blue Seven of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.SEVEN, "7_clubs.png")
BLUE_EIGHT_OF_CLUBS = Card("Blue Eight of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.EIGHT, "8_clubs.png")
BLUE_NINE_OF_CLUBS = Card("Blue Nine of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.NINE, "9_clubs.png")
BLUE_TEN_OF_CLUBS = Card("Blue Ten of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.TEN, "10_clubs.png")
BLUE_JACK_OF_CLUBS = Card("Blue Jack of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.JACK, "jack_clubs.png")
BLUE_KING_OF_CLUBS = Card("Blue King of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.KING, "king_clubs.png")
BLUE_QUEEN_OF_CLUBS = Card("Blue Queen of Clubs", CardType.BLUE, CardSuit.CLUBS, CardValue.QUEEN, "queen_clubs.png")
BLUE_ACE_OF_SPADES = Card("Blue Ace of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.ACE, "ace_spades.png")
BLUE_TWO_OF_SPADES = Card("Blue Two of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.TWO, "2_spades.png")
BLUE_THREE_OF_SPADES = Card("Blue Three of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.THREE, "3_spades.png")
BLUE_FOUR_OF_SPADES = Card("Blue Four of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.FOUR, "4_spades.png")
BLUE_FIVE_OF_SPADES = Card("Blue Five of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.FIVE, "5_spades.png")
BLUE_SIX_OF_SPADES = Card("Blue Six of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.SIX, "6_spades.png")
BLUE_SEVEN_OF_SPADES = Card("Blue Seven of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.SEVEN, "7_spades.png")
BLUE_EIGHT_OF_SPADES = Card("Blue Eight of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.EIGHT, "8_spades.png")
BLUE_NINE_OF_SPADES = Card("Blue Nine of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.NINE, "9_spades.png")
BLUE_TEN_OF_SPADES = Card("Blue Ten of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.TEN, "10_spades.png")
BLUE_JACK_OF_SPADES = Card("Blue Jack of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.JACK, "jack_spades.png")
BLUE_KING_OF_SPADES = Card("Blue King of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.KING, "king_spades.png")
BLUE_QUEEN_OF_SPADES = Card("Blue Queen of Spades", CardType.BLUE, CardSuit.SPADES, CardValue.QUEEN, "queen_spades.png")
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
RED_TWO_OF_HEARTS = Card("Red Two of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.TWO, "2_hearts.png")
RED_THREE_OF_HEARTS = Card("Red Three of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.THREE, "3_hearts.png")
RED_FOUR_OF_HEARTS = Card("Red Four of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.FOUR, "4_hearts.png")
RED_FIVE_OF_HEARTS = Card("Red Five of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.FIVE, "5_hearts.png")
RED_SIX_OF_HEARTS = Card("Red Six of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.SIX, "6_hearts.png")
RED_SEVEN_OF_HEARTS = Card("Red Seven of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.SEVEN, "7_hearts.png")
RED_EIGHT_OF_HEARTS = Card("Red Eight of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.EIGHT, "8_hearts.png")
RED_NINE_OF_HEARTS = Card("Red Nine of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.NINE, "9_hearts.png")
RED_TEN_OF_HEARTS = Card("Red Ten of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.TEN, "10_hearts.png")
RED_JACK_OF_HEARTS = Card("Red Jack of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.JACK, "jack_hearts.png")
RED_KING_OF_HEARTS = Card("Red King of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.KING, "king_hearts.png")
RED_QUEEN_OF_HEARTS = Card("Red Queen of Hearts", CardType.RED, CardSuit.HEARTS, CardValue.QUEEN, "queen_hearts.png")
RED_ACE_OF_DIAMONDS = Card("Red Ace of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.ACE, "ace_diamonds.png")
RED_TWO_OF_DIAMONDS = Card("Red Two of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.TWO, "2_diamonds.png")
RED_THREE_OF_DIAMONDS = Card("Red Three of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.THREE, "3_diamonds.png")
RED_FOUR_OF_DIAMONDS = Card("Red Four of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.FOUR, "4_diamonds.png")
RED_FIVE_OF_DIAMONDS = Card("Red Five of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.FIVE, "5_diamonds.png")
RED_SIX_OF_DIAMONDS = Card("Red Six of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.SIX, "6_diamonds.png")
RED_SEVEN_OF_DIAMONDS = Card("Red Seven of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.SEVEN, "7_diamonds.png")
RED_EIGHT_OF_DIAMONDS = Card("Red Eight of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.EIGHT, "8_diamonds.png")
RED_NINE_OF_DIAMONDS = Card("Red Nine of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.NINE, "9_diamonds.png")
RED_TEN_OF_DIAMONDS = Card("Red Ten of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.TEN, "10_diamonds.png")
RED_JACK_OF_DIAMONDS = Card("Red Jack of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.JACK, "jack_diamonds.png")
RED_KING_OF_DIAMONDS = Card("Red King of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.KING, "king_diamonds.png")
RED_QUEEN_OF_DIAMONDS = Card("Red Queen of Diamonds", CardType.RED, CardSuit.DIAMONDS, CardValue.QUEEN, "queen_diamonds.png")
RED_ACE_OF_CLUBS = Card("Red Ace of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.ACE, "ace_clubs.png")
RED_TWO_OF_CLUBS = Card("Red Two of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.TWO, "2_clubs.png")
RED_THREE_OF_CLUBS = Card("Red Three of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.THREE, "3_clubs.png")
RED_FOUR_OF_CLUBS = Card("Red Four of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.FOUR, "4_clubs.png")
RED_FIVE_OF_CLUBS = Card("Red Five of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.FIVE, "5_clubs.png")
RED_SIX_OF_CLUBS = Card("Red Six of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.SIX, "6_clubs.png")
RED_SEVEN_OF_CLUBS = Card("Red Seven of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.SEVEN, "7_clubs.png")
RED_EIGHT_OF_CLUBS = Card("Red Eight of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.EIGHT, "8_clubs.png")
RED_NINE_OF_CLUBS = Card("Red Nine of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.NINE, "9_clubs.png")
RED_TEN_OF_CLUBS = Card("Red Ten of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.TEN, "10_clubs.png")
RED_JACK_OF_CLUBS = Card("Red Jack of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.JACK, "jack_clubs.png")
RED_KING_OF_CLUBS = Card("Red King of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.KING, "king_clubs.png")
RED_QUEEN_OF_CLUBS = Card("Red Queen of Clubs", CardType.RED, CardSuit.CLUBS, CardValue.QUEEN, "queen_clubs.png")
RED_ACE_OF_SPADES = Card("Red Ace of Spades", CardType.RED, CardSuit.SPADES, CardValue.ACE, "ace_spades.png")
RED_TWO_OF_SPADES = Card("Red Two of Spades", CardType.RED, CardSuit.SPADES, CardValue.TWO, "2_spades.png")
RED_THREE_OF_SPADES = Card("Red Three of Spades", CardType.RED, CardSuit.SPADES, CardValue.THREE, "3_spades.png")
RED_FOUR_OF_SPADES = Card("Red Four of Spades", CardType.RED, CardSuit.SPADES, CardValue.FOUR, "4_spades.png")
RED_FIVE_OF_SPADES = Card("Red Five of Spades", CardType.RED, CardSuit.SPADES, CardValue.FIVE, "5_spades.png")
RED_SIX_OF_SPADES = Card("Red Six of Spades", CardType.RED, CardSuit.SPADES, CardValue.SIX, "6_spades.png")
RED_SEVEN_OF_SPADES = Card("Red Seven of Spades", CardType.RED, CardSuit.SPADES, CardValue.SEVEN, "7_spades.png")
RED_EIGHT_OF_SPADES = Card("Red Eight of Spades", CardType.RED, CardSuit.SPADES, CardValue.EIGHT, "8_spades.png")
RED_NINE_OF_SPADES = Card("Red Nine of Spades", CardType.RED, CardSuit.SPADES, CardValue.NINE, "9_spades.png")
RED_TEN_OF_SPADES = Card("Red Ten of Spades", CardType.RED, CardSuit.SPADES, CardValue.TEN, "10_spades.png")
RED_JACK_OF_SPADES = Card("Red Jack of Spades", CardType.RED, CardSuit.SPADES, CardValue.JACK, "jack_spades.png")
RED_KING_OF_SPADES = Card("Red King of Spades", CardType.RED, CardSuit.SPADES, CardValue.KING, "king_spades.png")
RED_QUEEN_OF_SPADES = Card("Red Queen of Spades", CardType.RED, CardSuit.SPADES, CardValue.QUEEN, "queen_spades.png")
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
        pygame.display.update()
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
        pygame.display.update()
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
        pygame.display.update()
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
        pygame.display.update()
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
            for x in range(len(Meta.PLAYERS)):
                BOARD_SQUARES[0].players.append(Meta.PLAYERS[x])
        pygame.display.update()
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
        pygame.display.update()
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
        pygame.display.update()
    elif Meta.CURRENT_STATE == ScreenState.BOARD_SYMBOLS_GUIDE:
        WINDOW.fill(PASTEL_GREEN)
        draw_text("Board Symbols Guide", MEDIUM_FONT, ORANGE, (960, 69))
        quit_button = Button("Quit", 960, 900, 60)
        back_button = Button("Back", 960, 800, 60)
        if quit_button.check_click():
            pygame.quit()
        elif back_button.check_click():
            Meta.CURRENT_STATE = ScreenState.GAME_INTRO_TWO
        draw_game_image(BLUE_CARD_SYMBOL, (320, 270), 2, True, (330, 80),
                        "Blue Card", "", "Draw 1 from the Blue Draw Deck")
        draw_game_image(RED_CARD_SYMBOL, (640, 270), 2, True, (330, 80),
                        "Red Card", "", "Draw 1 from the Red Draw Deck")
        check_hover_boxes()
        pygame.display.update()
    elif Meta.CURRENT_STATE == ScreenState.PLAYING_GAME:
        WINDOW.fill(WHITE)
        current_player = Meta.PLAYERS[Meta.CURRENT_PLAYER]
        draw_text(current_player.playerName + "'s Turn", SMALL_FONT, PLAYER_TO_COLOUR[current_player.playerNumber], (960, 30))
        game_board = pygame.Rect((480, 60), (960, 960))
        pygame.draw.rect(WINDOW, BLUE, game_board)
        roll_background = pygame.Rect((1460, 100), (440, 700))
        pygame.draw.rect(WINDOW, PASTEL_GREEN, roll_background, 0, 20)
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
                #  TODO: Draw Symbols
            for x in range(len(square.players)):
                player_image = pygame.image.load(square.players[x].playerPiece)
                WINDOW.blit(player_image, ((square.center[0] + PLAYER_TO_POSITION[x][0]) - 14, (square.center[1] + PLAYER_TO_POSITION[x][1]) - 14))
        if Meta.TURN_STAGE == TurnStage.ROLL_DICE:
            draw_text("Roll the d6 to move:", SMALL_FONT, BLACK, (1680, 240))
        quit_button = Button("Quit", 300, 540, 60)
        if quit_button.check_click():
            pygame.quit()
        pygame.display.update()


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
    if hover_box: Meta.HOVER_BOXES.append(("card", card, card_image, new_location))
    WINDOW.blit(card_image, new_location)


def draw_game_image(symbol, location, scale, hover_box = False, desc_size = (0, 0), *desc_lines):
    image_width = symbol[1][0] * scale
    image_height = symbol[1][1] * scale
    image = pygame.image.load(symbol[0])
    image = pygame.transform.scale(image, (image_width, image_height))
    new_location = (location[0] - (image_width/2), location[1] - (image_height/2))
    if hover_box:
        Meta.HOVER_BOXES.append(("board symbol", desc_lines, image, new_location, desc_size))
    WINDOW.blit(image, new_location)


def check_hover_boxes():
    for hover_box in Meta.HOVER_BOXES:
        if hover_box[0] == "card":
            card_rect = hover_box[2].get_rect()
            card_rect.topleft = hover_box[3]
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                if mouse_pos[0] <= 960:  # Card Desc. Horizontal Positioning
                    rect_left_position = mouse_pos[0] + 5
                else:
                    rect_left_position = mouse_pos[0] - hover_box[1].descRectSize[0]
                if mouse_pos[1] <= 540:
                    rect_top_position = mouse_pos[1] + 5
                else:
                    rect_top_position = mouse_pos[1] - hover_box[1].descRectSize[1]
                # Draw Card Name and Description
                card_desc_rect = pygame.Rect((rect_left_position, rect_top_position), hover_box[1].descRectSize)
                pygame.draw.rect(WINDOW, WHITE, card_desc_rect, 0, 5)
                draw_text(hover_box[1].displayName, TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + 5), False)
                for x in range(len(hover_box[1].descLines)):
                    draw_text(hover_box[1].descLines[x], TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + (20 * (x + 3))), False)
        elif hover_box[0] == "board symbol":
            card_rect = hover_box[2].get_rect()
            card_rect.topleft = hover_box[3]
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                if mouse_pos[0] <= 960:  # Card Back Desc. Horizontal Positioning
                    rect_left_position = mouse_pos[0] + 5
                else:
                    rect_left_position = mouse_pos[0] - hover_box[1].descRectSize[0]
                if mouse_pos[1] <= 540:
                    rect_top_position = mouse_pos[1] + 5
                else:
                    rect_top_position = mouse_pos[1] - hover_box[1].descRectSize[1]
                card_desc_rect = pygame.Rect((rect_left_position, rect_top_position), hover_box[4])
                pygame.draw.rect(WINDOW, WHITE, card_desc_rect, 0, 5)
                for x in range(len(hover_box[1])):
                    draw_text(hover_box[1][x], TINY_FONT, BLACK, (rect_left_position + 5, rect_top_position + ((20 * x) + 5)), False)


def main():  # Game Loop
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        Meta.HOVER_BOXES.clear()
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


if __name__ == "__main__":
    main()
