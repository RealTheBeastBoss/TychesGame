class Player:
    playerPiece = None
    blueDeck = None
    redDeck = None

    def __init__(self, player_number, given_name):
        self.playerName = given_name
        if player_number == 1:
            self.playerPiece = 1
        elif player_number == 2:
            self.playerPiece = 2
        elif player_number == 3:
            self.playerPiece = 3
        elif player_number == 4:
            self.playerPiece = 4
        else:
            self.playerPiece = 5
