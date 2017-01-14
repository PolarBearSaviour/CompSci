import pygame
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
        print(y)
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
