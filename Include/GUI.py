import pygame as pg, sys
from pygame.locals import *
from Include.board import emptyGrid as grid
#from Include.solve_sud import solve

#solve()

FPS = 10

WINDOWMULTIPLIER = 5
WINDOWSIZE = 90

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGRAY = (200, 200, 200)
RED = (255,0,0)

WINDOWWIDTH = int(WINDOWSIZE * WINDOWMULTIPLIER)
WINDOWHEIGHT = int(WINDOWSIZE * WINDOWMULTIPLIER)

SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3)
CELLSIZE = int(SQUARESIZE / 3)
#X = 0
#Y = 0
BOX = pg.Rect([0, 0, CELLSIZE, CELLSIZE])
#MARKCELLSIZE = CELLSIZE

def drawGrid():
    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE):  # draw vertical lines
        pg.draw.line(SCREEN, LIGHTGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
        pg.draw.line(SCREEN, LIGHTGRAY, (0, y), (WINDOWWIDTH, y))

    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE):  # draw vertical lines
        pg.draw.line(SCREEN, BLACK, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, SQUARESIZE):  # draw horizontal lines
        pg.draw.line(SCREEN, BLACK, (0, y), (WINDOWWIDTH, y))

    return None

def drawNumbers(grid):
    font = pg.font.SysFont('Arial MS', CELLSIZE)
    counterX = 0
    counterY = 0
    for row in grid:
        print(row)
        for number in row:
            if number != 0:
                SCREEN.blit(font.render("{}".format(number), True, BLACK), (CELLSIZE*counterX, CELLSIZE*counterY))
            counterX += 1
        counterY += 1
        counterX = 0
        #print(counterY)
        #print(counterX)


def drawMarked():
    pg.draw.rect(SCREEN, RED, BOX, 2)

def keys():
    keys = pg.key.get_pressed()

    if keys[pg.K_RIGHT] and BOX.x < 400:
        BOX.x += CELLSIZE
        #print(BOX.x, BOX.y)
        #return x
        #drawMarked(x, y)
    if keys[pg.K_LEFT] and BOX.x > 0:
        BOX.x -= CELLSIZE
        #print(BOX.x, BOX.y)
        #return x
        #drawMarked(x, y)
    if keys[pg.K_DOWN] and BOX.y < 400:
        BOX.y += CELLSIZE
        #print(BOX.x, BOX.y)
        #return y
        #drawMarked(x, y)
    if keys[pg.K_UP] and BOX.y > 0:
        BOX.y -= CELLSIZE
        #print(BOX.x, BOX.y)
        #return y
        #drawMarked(x, y)

    '''
    if keys[pg.K_1]:
    if keys[pg.K_2]:
    if keys[pg.K_3]:
    if keys[pg.K_4]:
    if keys[pg.K_5]:
    if keys[pg.K_6]:
    if keys[pg.K_7]:
    if keys[pg.K_8]:
    if keys[pg.K_9]:
    '''


def main():
    global SCREEN, FPSCLOCK
    pg.init()
    SCREEN = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pg.display.set_caption('Sudoku Solver')
    FPSCLOCK = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if pg.key.get_pressed()[pg.K_ESCAPE]:
                sys.exit()
        FPSCLOCK.tick(FPS)
        SCREEN.fill(WHITE)
        drawGrid()
        keys()
        drawMarked()
        drawNumbers(grid)
        pg.display.update()




if __name__=='__main__':
    main()

