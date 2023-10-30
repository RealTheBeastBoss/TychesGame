from game import *


class Player:
    def __init__(self, player_number, given_name):
        self.playerName = given_name
        self.blueDeck = []
        self.redDeck = []
        self.currentSquare = 0
        self.missNextTurn = False
        self.setNextRoll = None
        self.setPlayerRoll = None
        self.playerNumber = player_number
        if player_number == 0:
            self.playerColour = BLUE
        elif player_number == 1:
            self.playerColour = ORANGE
        elif player_number == 2:
            self.playerColour = GREEN
        elif player_number == 3:
            self.playerColour = PINK
        else:
            self.playerColour = RED
