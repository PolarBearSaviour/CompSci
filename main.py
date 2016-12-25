#####################################
##                                 ##
##                                 ##
##         github.com/jjydl        ##
##                                 ##
##                                 ##
#####################################

import pygame
from constants import *


########################
#      Wall Class      #
########################


class Wall(pygame.sprite.Sprite):

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
#     Player Class     #
########################


#player class, controls blob that cuts about the joint
class Player(pygame.sprite.Sprite):

    #change in direction
    change_x = 0
    change_y = 0

    #constructor
    def __init__(self, x, y):

        ##call constructor
        super().__init__()

        #create rectangle image with passed dimensions make it red
        self.image = pygame.Surface([8, 8])
        self.image.fill(RED)

        #create rectangle shape from rectangle image
        self.rect = self.image.get_rect()

        #set rectangle shape position
        self.rect.y = y
        self.rect.x = x

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
#     Stage Class      #
########################


class Comp(object):

    #list of walls and list of enemy sprites
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        #outer walls
        walls = [[0, 0, 15, 600, BLUE],
                 [585, 0, 15, 600, BLUE],
                 [15, 0, 570, 15, BLUE],
                 [15, 585, 570, 15, BLUE]
                ]


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

        #adds 15x15 block for every 1 in grid
        for row in range(0,29):
            for col in range(0,29):
                if grid[row][col]==1:
                    self.wall_list.add(Wall((col*15)+15,(row*15)+15,15,15,BLUE))


########################
#         Main         #
########################

#main function
def main():

    #initialise pygame engine
    pygame.init()

    #31x15,31x15 - logo is 29x29 and 1 at each end for gap around logo
    screen = pygame.display.set_mode([465, 465])

    #title
    pygame.display.set_caption('CompSci')

    #create player
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    #sets frame rate
    clock = pygame.time.Clock()

    #done flag
    done = False

    #game loop
    while not done:


        ########################
        #   Event Processing   #
        ########################


        #gets each event for frame
        for event in pygame.event.get():

            #quits if press x
            if event.type == pygame.QUIT:
                done = True

            #handles arrow key movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #player.resetSpeed()
                    player.setSpeedX(-3)
                    player.setSpeedY(0)
                elif event.key == pygame.K_RIGHT:
                    #player.resetSpeed()
                    player.setSpeedX(3)
                    player.setSpeedY(0)
                elif event.key == pygame.K_UP:
                    #player.resetSpeed()
                    player.setSpeedY(-3)
                    player.setSpeedX(0)
                elif event.key == pygame.K_DOWN:
                    #player.resetSpeed()
                    player.setSpeedY(3)
                    player.setSpeedX(0)


        ########################
        #      Game Logic      #
        ########################


        #move player
        player.move(Comp().wall_list)

        #ensures player doens't move off screen
        if player.rect.x < 0:
            player.rect.x = 0
        if player.rect.x > 457:
            player.rect.x = 457
        if player.rect.y < 0:
            player.rect.y = 0
        if player.rect.y > 457:
            player.rect.y = 457


        ########################
        #     Redraw Frame     #
        ########################

        #clears screen and adds white background
        screen.fill(WHITE)

        #draws sprites and walls
        movingsprites.draw(screen)
        Comp().wall_list.draw(screen)

        #shows drawn display
        pygame.display.flip()

        #sets frame rate limit
        clock.tick(60)

    #quits pygame engine when quit game
    pygame.quit()

#call main
if __name__ == "__main__":
    main()
