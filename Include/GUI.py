import pygame as pg, sys
from Include.board import emptyGrid as grid
import cv2 as cv
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from Include.solve_sud import solve, printGRIDDDD

#########################################################################################################
###########################################################################################################3

FPS = 10

WINDOWMULTIPLIER = 5
WINDOWSIZE = 90
BUTTON_SIZE = 15
BUTTON_WIDTH = 225

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGRAY = (200, 200, 200)
RED = (255,0,0)

WINDOWWIDTH = int(WINDOWSIZE * WINDOWMULTIPLIER)
WINDOWHEIGHT = int(WINDOWSIZE * WINDOWMULTIPLIER)
WINDOWHEIGHT_WITH_BUTTON = int(WINDOWSIZE * WINDOWMULTIPLIER) + int(BUTTON_SIZE*WINDOWMULTIPLIER)
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3)
CELLSIZE = int(SQUARESIZE / 3)
#X = 0
#Y = 0
BUTTON1_COORDS = pg.Rect([0, WINDOWHEIGHT, BUTTON_WIDTH, 75])
BUTTON2_COORDS = pg.Rect([225, WINDOWHEIGHT, BUTTON_WIDTH, 75])
BOX = pg.Rect([0, 0, CELLSIZE, CELLSIZE])
#MARKCELLSIZE = CELLSIZE

def importFile():
    TK.title('Importing Image')
    #TK.iconbitmap('')
    TK.filename = fd.askopenfilename(initialdir="/Include", title = "Select a file",
                                     filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    imLabel = Label(TK, text=TK.filename).pack()
    imageImp = ImageTk.PhotoImage(Image.open(TK.filename))
    imageImLabel = Label(image=imageImp).pack()
    #print(imageImp)
    if len(TK.filename) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        imgcv = cv.imread(TK.filename, 0)
        cv.imshow('img', imgcv)
    TK.mainloop()

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

    ### Draw Buttons
    pg.draw.rect(SCREEN,BLACK, BUTTON1_COORDS, 2)
    pg.draw.rect(SCREEN,BLACK, BUTTON2_COORDS, 2)

    return None


def drawNumbers(grid):
    font = pg.font.SysFont('Arial MS', CELLSIZE)
    counterX = 0
    counterY = 0
    for row in grid:
        for number in row:
            if number != 0:
                SCREEN.blit(font.render("{}".format(number), True, BLACK), (CELLSIZE*counterX+15, CELLSIZE*counterY+10))
            counterX += 1
        counterY += 1
        counterX = 0


def drawLabels():
    font = pg.font.SysFont('Arial MS', CELLSIZE)
    SCREEN.blit(font.render("IMPORT", True, BLACK), (50, 475))
    SCREEN.blit(font.render("SOLVE", True, RED), (275, 475))

def drawMarked():
    if BOX.y <= WINDOWHEIGHT:
        pg.draw.rect(SCREEN, RED, BOX, 2)
    if BOX.y > WINDOWHEIGHT and BOX.x < BUTTON_WIDTH:
        pg.draw.rect(SCREEN, RED, BUTTON1_COORDS, 2)
    if BOX.y > WINDOWHEIGHT and BOX.x >= BUTTON_WIDTH:
        pg.draw.rect(SCREEN, RED, BUTTON2_COORDS, 2)


def keys(grid):
    keys = pg.key.get_pressed()

    if BOX.y < WINDOWHEIGHT:
        if keys[pg.K_RIGHT] and BOX.x < WINDOWWIDTH-CELLSIZE:
            BOX.x += CELLSIZE
            print(BOX.x, BOX.y)
            #return x
            #drawMarked(x, y)
        if keys[pg.K_LEFT] and BOX.x > 0:
            BOX.x -= CELLSIZE
            print(BOX.x, BOX.y)
            #return x
            #drawMarked(x, y)
        if keys[pg.K_DOWN] and BOX.y < WINDOWHEIGHT_WITH_BUTTON:
            BOX.y += CELLSIZE
            print(BOX.x, BOX.y)
            #return y
            #drawMarked(x, y)
        if keys[pg.K_UP] and BOX.y > 0:
            BOX.y -= CELLSIZE
            print(BOX.x, BOX.y)

            #return y
            #drawMarked(x, y)
    if BOX.y >= WINDOWHEIGHT:
        if keys[pg.K_RIGHT] and BOX.x <= 200:
            BOX.x += BUTTON_WIDTH
            print(BOX.x, BOX.y)
            #return x
            #drawMarked(x, y)
        if keys[pg.K_LEFT] and BOX.x >= BUTTON_WIDTH:
            BOX.x -= BUTTON_WIDTH
            print(BOX.x, BOX.y)
            #return x
            #drawMarked(x, y)
        if keys[pg.K_DOWN] and BOX.y < WINDOWHEIGHT_WITH_BUTTON:
            BOX.y += CELLSIZE*1.5
            print(BOX.x, BOX.y)
            #return y
            #drawMarked(x, y)
        if keys[pg.K_UP] and BOX.y > 0:
            BOX.y -= CELLSIZE*1.5
            print(BOX.x, BOX.y)

            BOX.x = (WINDOWHEIGHT-CELLSIZE)/2
            BOX.y = WINDOWHEIGHT-CELLSIZE
        if BOX.x < 225 and BOX.y >= 425:
            if keys[pg.K_RETURN]:
                print("Import ENTER CLICKED")
                importFile()
        if BOX.x >= 225 and BOX.y >= 425:
            if keys[pg.K_RETURN]:
                #print("Solve:", solve(grid))
                #gridX = solve(grid)
                #print("GridX: ", gridX)
                printGRIDDDD(grid)
                return solve(grid)
                #grid = solve(grid)
                #print('grid GUI', solve(grid))
                #drawNumbers(grid)
            #return y
            #drawMarked(x, y)
    gridI = BOX.y//CELLSIZE
    gridJ = BOX.x//CELLSIZE

    if keys[pg.K_1]:
        grid[gridI][gridJ]=1
    if keys[pg.K_2]:
        grid[gridI][gridJ]=2
    if keys[pg.K_3]:
        grid[gridI][gridJ]=3
    if keys[pg.K_4]:
        grid[gridI][gridJ]=4
    if keys[pg.K_5]:
        grid[gridI][gridJ]=5
    if keys[pg.K_6]:
        grid[gridI][gridJ]=6
    if keys[pg.K_7]:
        grid[gridI][gridJ]=7
    if keys[pg.K_8]:
        grid[gridI][gridJ]=8
    if keys[pg.K_9]:
        grid[gridI][gridJ]=9
    if keys[pg.K_0] or keys[pg.K_BACKSPACE]:
        grid[gridI][gridJ]=0


def main():
    global SCREEN, FPSCLOCK, TK
    pg.init()
    TK = tk.Tk()
    SCREEN = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT_WITH_BUTTON))
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
        keys(grid)
        drawMarked()
        drawNumbers(grid)
        drawLabels()
        pg.display.update()


if __name__=='__main__':
    main()

