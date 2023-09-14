import os
import pygame
import random
from card import *
from enum import Enum

class ScreenState(Enum):
    START = 1
    NEW_MENU = 2


pygame.font.init()
WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tyche's Game")
FPS = 60
BIG_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 90)
SMALL_FONT = pygame.font.Font(os.path.join("Fonts", "beastboss_font.ttf"), 30)

# Game Colours
BLUE = (0, 0, 255)
ORANGE = (255, 102, 0)

# Game Cards
# region
BLUE_ACE_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.ACE)
BLUE_TWO_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.TWO)
BLUE_THREE_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.THREE)
BLUE_FOUR_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.FOUR)
BLUE_FIVE_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.FIVE)
BLUE_SIX_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.SIX)
BLUE_SEVEN_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.SEVEN)
BLUE_EIGHT_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.EIGHT)
BLUE_NINE_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.NINE)
BLUE_TEN_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.TEN)
BLUE_JACK_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.JACK)
BLUE_KING_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.KING)
BLUE_QUEEN_OF_HEARTS = Card(CardType.BLUE, CardSuit.HEARTS, CardValue.QUEEN)
BLUE_ACE_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.ACE)
BLUE_TWO_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.TWO)
BLUE_THREE_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.THREE)
BLUE_FOUR_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.FOUR)
BLUE_FIVE_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.FIVE)
BLUE_SIX_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.SIX)
BLUE_SEVEN_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.SEVEN)
BLUE_EIGHT_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.EIGHT)
BLUE_NINE_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.NINE)
BLUE_TEN_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.TEN)
BLUE_JACK_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.JACK)
BLUE_KING_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.KING)
BLUE_QUEEN_OF_DIAMONDS = Card(CardType.BLUE, CardSuit.DIAMONDS, CardValue.QUEEN)
BLUE_ACE_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.ACE)
BLUE_TWO_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.TWO)
BLUE_THREE_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.THREE)
BLUE_FOUR_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.FOUR)
BLUE_FIVE_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.FIVE)
BLUE_SIX_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.SIX)
BLUE_SEVEN_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.SEVEN)
BLUE_EIGHT_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.EIGHT)
BLUE_NINE_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.NINE)
BLUE_TEN_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.TEN)
BLUE_JACK_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.JACK)
BLUE_KING_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.KING)
BLUE_QUEEN_OF_CLUBS = Card(CardType.BLUE, CardSuit.CLUBS, CardValue.QUEEN)
BLUE_ACE_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.ACE)
BLUE_TWO_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.TWO)
BLUE_THREE_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.THREE)
BLUE_FOUR_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.FOUR)
BLUE_FIVE_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.FIVE)
BLUE_SIX_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.SIX)
BLUE_SEVEN_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.SEVEN)
BLUE_EIGHT_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.EIGHT)
BLUE_NINE_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.NINE)
BLUE_TEN_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.TEN)
BLUE_JACK_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.JACK)
BLUE_KING_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.KING)
BLUE_QUEEN_OF_SPADES = Card(CardType.BLUE, CardSuit.SPADES, CardValue.QUEEN)
BLUE_RED_JOKER = Card(CardType.BLUE, CardSuit.RED, CardValue.JOKER)
BLUE_BLUE_JOKER = Card(CardType.BLUE, CardSuit.BLUE, CardValue.JOKER)
BLUE_DRAW_DECK = [BLUE_ACE_OF_HEARTS, BLUE_TWO_OF_HEARTS, BLUE_THREE_OF_HEARTS, BLUE_FOUR_OF_HEARTS, BLUE_FIVE_OF_HEARTS, BLUE_SIX_OF_HEARTS,
                  BLUE_SEVEN_OF_HEARTS, BLUE_EIGHT_OF_HEARTS, BLUE_NINE_OF_HEARTS, BLUE_TEN_OF_HEARTS, BLUE_JACK_OF_HEARTS, BLUE_KING_OF_HEARTS,
                  BLUE_QUEEN_OF_HEARTS, BLUE_ACE_OF_DIAMONDS, BLUE_TWO_OF_DIAMONDS, BLUE_THREE_OF_DIAMONDS, BLUE_FOUR_OF_DIAMONDS, BLUE_FIVE_OF_DIAMONDS,
                  BLUE_SIX_OF_DIAMONDS, BLUE_SEVEN_OF_DIAMONDS, BLUE_EIGHT_OF_DIAMONDS, BLUE_NINE_OF_DIAMONDS, BLUE_TEN_OF_DIAMONDS, BLUE_JACK_OF_DIAMONDS,
                  BLUE_KING_OF_DIAMONDS, BLUE_QUEEN_OF_DIAMONDS, BLUE_ACE_OF_CLUBS, BLUE_TWO_OF_CLUBS, BLUE_THREE_OF_CLUBS, BLUE_FOUR_OF_CLUBS,
                  BLUE_FIVE_OF_CLUBS, BLUE_SIX_OF_CLUBS, BLUE_SEVEN_OF_CLUBS, BLUE_EIGHT_OF_CLUBS, BLUE_NINE_OF_CLUBS, BLUE_TEN_OF_CLUBS,
                  BLUE_JACK_OF_CLUBS, BLUE_KING_OF_CLUBS, BLUE_QUEEN_OF_CLUBS, BLUE_ACE_OF_SPADES, BLUE_TWO_OF_SPADES, BLUE_THREE_OF_SPADES,
                  BLUE_FOUR_OF_SPADES, BLUE_FIVE_OF_SPADES, BLUE_SIX_OF_SPADES, BLUE_SEVEN_OF_SPADES, BLUE_EIGHT_OF_SPADES, BLUE_NINE_OF_SPADES,
                  BLUE_TEN_OF_SPADES, BLUE_JACK_OF_SPADES, BLUE_KING_OF_SPADES, BLUE_QUEEN_OF_SPADES, BLUE_BLUE_JOKER, BLUE_RED_JOKER]
random.shuffle(BLUE_DRAW_DECK)
RED_ACE_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.ACE)
RED_TWO_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.TWO)
RED_THREE_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.THREE)
RED_FOUR_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.FOUR)
RED_FIVE_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.FIVE)
RED_SIX_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.SIX)
RED_SEVEN_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.SEVEN)
RED_EIGHT_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.EIGHT)
RED_NINE_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.NINE)
RED_TEN_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.TEN)
RED_JACK_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.JACK)
RED_KING_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.KING)
RED_QUEEN_OF_HEARTS = Card(CardType.RED, CardSuit.HEARTS, CardValue.QUEEN)
RED_ACE_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.ACE)
RED_TWO_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.TWO)
RED_THREE_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.THREE)
RED_FOUR_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.FOUR)
RED_FIVE_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.FIVE)
RED_SIX_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.SIX)
RED_SEVEN_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.SEVEN)
RED_EIGHT_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.EIGHT)
RED_NINE_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.NINE)
RED_TEN_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.TEN)
RED_JACK_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.JACK)
RED_KING_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.KING)
RED_QUEEN_OF_DIAMONDS = Card(CardType.RED, CardSuit.DIAMONDS, CardValue.QUEEN)
RED_ACE_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.ACE)
RED_TWO_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.TWO)
RED_THREE_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.THREE)
RED_FOUR_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.FOUR)
RED_FIVE_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.FIVE)
RED_SIX_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.SIX)
RED_SEVEN_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.SEVEN)
RED_EIGHT_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.EIGHT)
RED_NINE_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.NINE)
RED_TEN_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.TEN)
RED_JACK_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.JACK)
RED_KING_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.KING)
RED_QUEEN_OF_CLUBS = Card(CardType.RED, CardSuit.CLUBS, CardValue.QUEEN)
RED_ACE_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.ACE)
RED_TWO_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.TWO)
RED_THREE_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.THREE)
RED_FOUR_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.FOUR)
RED_FIVE_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.FIVE)
RED_SIX_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.SIX)
RED_SEVEN_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.SEVEN)
RED_EIGHT_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.EIGHT)
RED_NINE_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.NINE)
RED_TEN_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.TEN)
RED_JACK_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.JACK)
RED_KING_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.KING)
RED_QUEEN_OF_SPADES = Card(CardType.RED, CardSuit.SPADES, CardValue.QUEEN)
RED_RED_JOKER = Card(CardType.RED, CardSuit.RED, CardValue.JOKER)
RED_BLUE_JOKER = Card(CardType.RED, CardSuit.BLUE, CardValue.JOKER)
RED_DRAW_DECK = [RED_ACE_OF_HEARTS, RED_TWO_OF_HEARTS, RED_THREE_OF_HEARTS, RED_FOUR_OF_HEARTS, RED_FIVE_OF_HEARTS, RED_SIX_OF_HEARTS,
                  RED_SEVEN_OF_HEARTS, RED_EIGHT_OF_HEARTS, RED_NINE_OF_HEARTS, RED_TEN_OF_HEARTS, RED_JACK_OF_HEARTS, RED_KING_OF_HEARTS,
                  RED_QUEEN_OF_HEARTS, RED_ACE_OF_DIAMONDS, RED_TWO_OF_DIAMONDS, RED_THREE_OF_DIAMONDS, RED_FOUR_OF_DIAMONDS, RED_FIVE_OF_DIAMONDS,
                  RED_SIX_OF_DIAMONDS, RED_SEVEN_OF_DIAMONDS, RED_EIGHT_OF_DIAMONDS, RED_NINE_OF_DIAMONDS, RED_TEN_OF_DIAMONDS, RED_JACK_OF_DIAMONDS,
                  RED_KING_OF_DIAMONDS, RED_QUEEN_OF_DIAMONDS, RED_ACE_OF_CLUBS, RED_TWO_OF_CLUBS, RED_THREE_OF_CLUBS, RED_FOUR_OF_CLUBS,
                  RED_FIVE_OF_CLUBS, RED_SIX_OF_CLUBS, RED_SEVEN_OF_CLUBS, RED_EIGHT_OF_CLUBS, RED_NINE_OF_CLUBS, RED_TEN_OF_CLUBS,
                  RED_JACK_OF_CLUBS, RED_KING_OF_CLUBS, RED_QUEEN_OF_CLUBS, RED_ACE_OF_SPADES, RED_TWO_OF_SPADES, RED_THREE_OF_SPADES,
                  RED_FOUR_OF_SPADES, RED_FIVE_OF_SPADES, RED_SIX_OF_SPADES, RED_SEVEN_OF_SPADES, RED_EIGHT_OF_SPADES, RED_NINE_OF_SPADES,
                  RED_TEN_OF_SPADES, RED_JACK_OF_SPADES, RED_KING_OF_SPADES, RED_QUEEN_OF_SPADES, RED_BLUE_JOKER, RED_RED_JOKER]
random.shuffle(RED_DRAW_DECK)
DISCARD_PILE = None
# endregion


class Button:
    def __init__(self, text, x_pos, y_pos, width, height, enabled = True):
        self.text = text
        self.xPos = x_pos
        self.yPos = y_pos
        self.width = width
        self.height = height
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_rect = pygame.rect.Rect((self.xPos, self.yPos), (self.width, self.height))
        if not self.check_hover():
            button_text = SMALL_FONT.render(self.text, True, ORANGE)
            pygame.draw.rect(WINDOW, BLUE, button_rect, 0, 5)
            pygame.draw.rect(WINDOW, ORANGE, button_rect, 3, 5)
        else:
            button_text = SMALL_FONT.render(self.text, True, BLUE)
            pygame.draw.rect(WINDOW, ORANGE, button_rect, 0, 5)
            pygame.draw.rect(WINDOW, BLUE, button_rect, 3, 5)
        text_width_offset = button_text.get_width() / 2
        text_height_offset = button_text.get_height() / 2
        WINDOW.blit(button_text, ((self.xPos + (self.width/2) - text_width_offset), (self.yPos + (self.height/2)) - text_height_offset))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.xPos, self.yPos), (self.width, self.height))
        if button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.xPos, self.yPos), (self.width, self.height))
        return left_click and button_rect.collidepoint(mouse_pos)


def draw_window(state):
    if state == ScreenState.START:
        WINDOW.fill(BLUE)
        draw_text("Tyche's Game", BIG_FONT, ORANGE, (WIDTH/2, 69))
        quit_button = Button("Quit", (WIDTH/2) - 40, 300, 80, 60)
        if quit_button.check_click():
            pygame.quit()
        new_game_button = Button("New Game", (WIDTH/2) - 90, 200, 180, 60)
        pygame.display.update()
        if new_game_button.check_click():
            return ScreenState.NEW_MENU
        return ScreenState.START
    elif state == ScreenState.NEW_MENU:
        WINDOW.fill(ORANGE)
        quit_button = Button("Quit", (WIDTH/2) - 40, 300, 80, 60)
        if quit_button.check_click():
            pygame.quit()
        pygame.display.update()
        return ScreenState.NEW_MENU


def draw_text(text, font, colour, location):  # Draws text centered on a location
    text_surface = font.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    WINDOW.blit(text_surface, (location[0] - (text_width/2), location[1] - (text_height/2)))


def main():  # Game Loop
    clock = pygame.time.Clock()
    player_count = 2  # 2 while testing
    current_state = ScreenState.START
    while True:
        clock.tick(FPS)
        # Game Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current_state = draw_window(current_state)


if __name__ == "__main__":
    main()
