from meta import *


class Player:
    def __init__(self, player_number, given_name):
        self.playerName = given_name
        self.blueDeck = []
        self.redDeck = []
        self.currentSquare = 0
        self.missNextTurn = False
        self.setNextRoll = None
        self.playerNumber = player_number
        if player_number == 0:
            self.playerPiece = PLAYER_ONE
            self.playerColour = BLUE
        elif player_number == 1:
            self.playerPiece = PLAYER_TWO
            self.playerColour = ORANGE
        elif player_number == 2:
            self.playerPiece = PLAYER_THREE
            self.playerColour = GREEN
        elif player_number == 3:
            self.playerPiece = PLAYER_FOUR
            self.playerColour = PINK
        else:
            self.playerPiece = PLAYER_FIVE
            self.playerColour = RED
