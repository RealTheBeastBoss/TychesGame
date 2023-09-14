from enum import Enum


class CardType(Enum):
    BLUE = 1
    RED = 2


class CardSuit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4
    RED = 5
    BLUE = 6


class CardValue(Enum):
    JOKER = 0
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    KING = 12
    QUEEN = 13


class Card:
    def __init__(self, colour, suit, value):
        self.cardType = colour
        self.cardSuit = suit
        self.cardValue = value
