from Include.board import printCheckedGrid as pgrid
#from Include.board import emptyGrid as printCheckedGrid #GRID
import numpy as np
'''
print('Sudoku to solve:')
printCheckedGrid()
print(' ')
'''


def isCorrect(GRID, x, y, num):
    for i in range(0, 9):
        if GRID[x][i] == num:
            return False

    for i in range(0, 9):
        if GRID[i][y] == num:
            return False

    startX = (x // 3) * 3
    startY = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if GRID[startX + i][startY + i] == num:
                return False
    return True


def solve(GRID):
    for x in range(len(GRID)):
        for y in range(len(GRID)):
            #print(y,x)
            if GRID[x][y] == 0:
                for num in range(1, 10):
                    if isCorrect(GRID, x, y, num):
                        GRID[x][y] = num
                        solve(GRID)
                        GRID[x][y] = 0
                return
    GRIDZ = GRID
    print('GRIDZ', GRIDZ)
    return GRIDZ
    #print('Grid:', GRID)
    #pgrid(GRID)
    #print('chuj', GRID)
    #print('Solved Sudoku:')
    #printCheckedGrid(GRID)
    #print('grid SOLVE',GRID)

def printGRIDDDD(GRID):
    bob = solve(GRID)
    print('solve', bob)
    print('printGRIDDDD',GRID)
#print('solve(grid)',solve(grid))

#solve()
