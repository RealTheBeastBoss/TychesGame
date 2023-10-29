import pygame


class Square:
    def __init__(self, symbol, center, barrier = False, monster_health = 0, key = 0):
        self.symbol = symbol
        self.center = center
        self.players = []
        self.hasBarrier = barrier
        self.monsterHealth = monster_health
        self.monsterAwake = False
        self.keyLocation = key
        self.currentRect = pygame.Rect((center[0] - 44, center[1] - 44), (89, 89))
