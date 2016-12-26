from constants import *
import pygame

def setupFonts(size, font = None):
    pygame.font.init()
    if font == None:
        font = pygame.font.get_default_font()
    fontRender = pygame.font.Font(font, size)
    return font_render

def keepPlayerOnScreen(player):
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x > SCREEN_SIZE['WIDTH'] - player.rect.width:
        player.rect.x = SCREEN_SIZE['WIDTH'] - player.rect.width
    if player.rect.y < 0:
        player.rect.y = 0
    if player.rect.y > SCREEN_SIZE['HEIGHT'] - player.rect.height:
        player.rect.y = SCREEN_SIZE['HEIGHT'] - player.rect.height
