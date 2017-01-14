import pygame
from constants import WHITE
class ScreenManager:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode([self._width, self._height])

    def returnScreenDim(self):
        return {"height":self._height, "width":self._width}

    def setFrameRate(self, FPS):
        self._clock = pygame.time.Clock()
        self._clock.tick(FPS)

    def setupFonts(self, font = None):
        pygame.font.init()
        if font == None:
            font = pygame.font.get_default_font()
        self._fontRender = pygame.font.Font(font, size)

    def renderText(self, text, position, colour):
        label = self._fontRender(text, 1, colour)
        self._screen.bilt(label, position)

    def drawScreen(self, sprites):
        self._screen.fill(WHITE)
        sprites.draw(self._screen)
        pygame.display.flip()

    def mapLevelToGrid(self, row, column):
        return {
            "width" : self._width//(row+1),
            "height" : self._height//(column+1)
        }
