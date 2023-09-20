import pygame


class Square:
    def __init__(self, square_symbol, center, barrier = False):
        self.symbol = square_symbol
        self.center = center
        self.players = []
        self.hasBarrier = barrier
        self.currentRect = pygame.Rect((center[0] - 44, center[1] - 44), (89, 89))
