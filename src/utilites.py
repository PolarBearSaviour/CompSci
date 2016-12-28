from constants import *
import pygame



def setupFonts(size, font = None):
    pygame.font.init()
    if font == None:
        font = pygame.font.get_default_font()
    fontRender = pygame.font.Font(font, size)
    return fontRender

def handleEvents(players):
    #gets each event for frame
    for event in pygame.event.get():
        #quits if press x
        if event.type == pygame.QUIT:
            return True

        #handles arrow key movement
        if event.type == pygame.KEYDOWN:
            for index in range(len(players)):
                players[index].handleKeyBoardEvent(event)
        return False

def drawScreen(screen, playArea, movingsprites):
    #clears screen and adds white background
    screen.fill(WHITE)

    #draws sprites and walls
    movingsprites.draw(screen)
    playArea.wall_list.draw(screen)
    playArea.objectives.draw(screen)

    #shows drawn display
    pygame.display.flip()

def renderLabel(text, fontRender, position, screen):
    label = fontRender.render(text, 1, BLACK)
    screen.blit(label, position)

def updateObjects(players, playArea):
    #move player
    for index in range(len(players)):
        players[index].move(playArea.wall_list, playArea.objectives)

    #ensures player doens't move off screen
    for index in range(len(players)):
        keepPlayerOnScreen(players[index])



def keepPlayerOnScreen(player):
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x > SCREEN_SIZE['WIDTH'] - player.rect.width:
        player.rect.x = SCREEN_SIZE['WIDTH'] - player.rect.width
    if player.rect.y < 0:
        player.rect.y = 0
    if player.rect.y > SCREEN_SIZE['HEIGHT'] - player.rect.height:
        player.rect.y = SCREEN_SIZE['HEIGHT'] - player.rect.height
