import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (9, 72, 123)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
SCREEN_SIZE = {'WIDTH': 465, 'HEIGHT': 465}
MAP_KEY = {"BLANK": 0, "WALL": 1, "SPAWN": 2, "OBJECTIVES": 3, "POWER-UPS" : 4, "TRAPS" : 5}
PLAYER_KEYS = [{"LEFT": pygame.K_LEFT, "RIGHT" : pygame.K_RIGHT, "UP" : pygame.K_UP, "DOWN" : pygame.K_DOWN}, \
                {"LEFT" : 97, "RIGHT" : 100, "UP": 119, "DOWN": 115}]
