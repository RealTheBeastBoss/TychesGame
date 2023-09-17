from meta import *


class Player:
    def __init__(self, player_number, given_name):
        self.playerName = given_name
        self.blueDeck = []
        self.redDeck = []
        self.currentSquare = 0
        self.playerNumber = player_number
        if player_number == 0:
            self.playerPiece = PLAYER_ONE
        elif player_number == 1:
            self.playerPiece = PLAYER_TWO
        elif player_number == 2:
            self.playerPiece = PLAYER_THREE
        elif player_number == 3:
            self.playerPiece = PLAYER_FOUR
        else:
            self.playerPiece = PLAYER_FIVE
