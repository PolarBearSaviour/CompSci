from Level import Level
from ScreenManager import ScreenManager
from constants import MAP_KEY, BLUE, PLAYER_KEYS
from Screen_element import *
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self._level = Level('firstLevel')
        self._screen = ScreenManager(465, 465)
        self._walls = pygame.sprite.Group()
        self._sprites = pygame.sprite.Group()

    def initLevel(self):

        self._level.init()
        row = self._level.accessMetadata('number-of-rows')
        columns = self._level.accessMetadata('number-of-columns')
        secSize = self._screen.mapLevelToGrid(row, columns)
        print(secSize)
        level = self._level.getLevel()
        print(level)
        xPos = lambda width, x :(x*width) + width
        yPos = lambda height, y: (y*height) + height

        numPlayers = 0
        for y, row in enumerate(level):
            for x, column in enumerate(row):
                if column == MAP_KEY['WALL']:
                    self._walls.add(Block(xPos(secSize['width'], x), yPos(secSize['height'], y), 15, 15, BLUE))
                elif column == MAP_KEY['SPAWN']:
                    print(column)
                    print("({0}, {1})".format(x,y))
                    self._sprites.add(Player(xPos(secSize['width'], x), yPos(secSize['height'], y), PLAYER_KEYS[numPlayers], BLUE))

    def initScreen(self):
        self._screen.setFrameRate(60)

    def tick(self):
        self._screen.drawScreen([self._walls, self._sprites])

    def run(self):
        self.initLevel()
        self.initScreen()
        finished = False
        while not finished:
            self.tick()

def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
