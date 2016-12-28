#####################################
##                                 ##
##                                 ##
##         github.com/jjydl        ##
##                                 ##
##                                 ##
#####################################

import pygame
import random
from constants import *
from utilites import *

########################
#      Wall Class      #
########################


class Block(pygame.sprite.Sprite):
    #constructor
    def __init__(self, x, y, width, height, colour):

        #call constructor
        super().__init__()

        #create rectangle image with passed dimensions and colour
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        #create rectangle shape from rectangle image
        self.rect = self.image.get_rect()

        #set rectangle shape position
        self.rect.y = y
        self.rect.x = x


########################
#     Block Class     #
########################


#moving block class, implements functionality for blocks that cut about the joint
class MovingBlock(Block):

    #constructor
    def __init__(self, x, y, height, width, colour):
        ##call constructor
        super().__init__(x, y, height, width, colour)
        self.change_x = 0
        self.change_y = 0

    #sets new x direction of player
    def setSpeedX(self, x):
        self.change_x = x

    #sets new x direction of player
    def setSpeedY(self, y):
        self.change_y = y

    #stops player moving
    def resetSpeed(self):
        self.change_x = 0
        self.change_y = 0

    #determines new position
    def move(self, walls):

        if not self.change_x == 0:
            #moves left or right
            self.rect.x += self.change_x

            #checks if player collides with wall, doesn't remove walls
            block_hit_list = pygame.sprite.spritecollide(self, walls, False)
            for block in block_hit_list:
                #if player moves right, set player right side to left side of wall
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                #else do the oppisite with left
                else:
                    self.rect.left = block.rect.right
        else:
            #moves up or down
            self.rect.y += self.change_y

            #checks if player collides with wall, doesn't remove walls
            block_hit_list = pygame.sprite.spritecollide(self, walls, False)
            for block in block_hit_list:
                #if player moves down, set player bottom side to bottom side of wall
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                #else do the oppisite with up
                else:
                    self.rect.top = block.rect.bottom



########################
#     Player Class     #
########################
class Player(MovingBlock):

    def __init__(self, x, y, inputs, colour):
        super().__init__(x,y, 8, 8, colour)
        self._keys = inputs
        self._score = 0
    def getScore(self):
        return self._score

    def handleKeyBoardEvent(self, event):

        if self._keys['LEFT'] == event.key:
            self.change_x = -1
            self.change_y = 0
        elif self._keys['RIGHT'] == event.key:
            self.change_x = 1
            self.change_y = 0
        elif self._keys['DOWN'] == event.key:
            self.change_y = 1
            self.change_x = 0
        elif self._keys['UP'] == event.key:
            self.change_y = -1
            self.change_x = 0

    def increaseScore(self, objective):
        self._score += objective.worth

    def move(self, walls, objectives):
        MovingBlock.move(self, walls)
        if not self.change_x == 0:
            hitList = pygame.sprite.spritecollide(self, objectives, True)
            for objective in hitList:
                self.increaseScore(objective)


########################
#     Objective Class  #
########################
class Objective(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 5, 5, PURPLE)
        self.worth = random.randint(1, 5)



########################
#     Stage Class      #
########################
class Level:
    def __init__(self, levelLayout):
        self.wall_list = pygame.sprite.Group()
        self.objectives = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.levelURL = '../level/' + levelLayout
        self.level

    def readInLevel(self):
        f = open(self.levelURL, 'w')
        for line in f:
            print(line)

class Comp:


    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.objectives = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        #compsci logo
        grid = [[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
                [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
                [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
                [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
                ]

        occupied = True
        numObjective = 0
        while occupied and not numObjective == 10:
            row = random.randint(0, 28)
            col = random.randint(0, 28)
            if grid[row][col] == 0:
                grid[row][col] = 2
                numObjective += 1

        #adds 15x15 block for every 1 in grid
        for row in range(0,29):
            for col in range(0,29):
                if grid[row][col]==1:
                    self.wall_list.add(Block((col*15)+15,(row*15)+15,15,15,BLUE))
                elif grid[row][col] == 2:
                    self.objectives.add(Objective((col*15) + 18, (row*15) + 18))


########################
#         Main         #
########################


#main function
def main():

    #initialise pygame engine
    pygame.init()

    #31x15,31x15 - logo is 29x29 and 1 at each end for gap around logo
    screen = pygame.display.set_mode([SCREEN_SIZE['WIDTH'], SCREEN_SIZE['HEIGHT']])

    #title
    pygame.display.set_caption('CompSci')
    inputs1 = {"LEFT": pygame.K_LEFT, "RIGHT" : pygame.K_RIGHT, "UP" : pygame.K_UP, "DOWN" : pygame.K_DOWN}
    input2 = {"LEFT" : 97, "RIGHT" : 100, "UP": 119, "DOWN": 115}
    #create player
    players = [Player(50, 50, inputs1, RED), Player(100, 100, input2, GREEN)]
    movingsprites = pygame.sprite.Group()

    for index in range(len(players)):
        movingsprites.add(players[index])

    #sets frame rate
    clock = pygame.time.Clock()
    #sets frame rate limit
    clock.tick(60)

    fontRender = setupFonts(15)

    #done flag
    done = False
    playArea = Comp()
    #game loop
    while not done:
        handleEvents(players)
        drawScreen(screen, playArea, movingsprites)

        x = 0
        for index in range(len(players)):
            renderLabel("Player {}: {}".format(index+1, players[index].getScore()), fontRender, (x, 0), screen)
            x += 300

        updateObjects(players, playArea)


        done = len(playArea.objectives) == 0

    # TODO: check what player is the winner and then declare them so! Along with tightening up the controls

    #quits pygame engine when quit game
    pygame.quit()

#call main
if __name__ == "__main__":
    main()
