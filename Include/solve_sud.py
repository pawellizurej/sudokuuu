# from board import printCheckedGrid as pgrid
from Include.board import emptyGrid as GRID, printCheckedGrid

print('Sudoku to solve:')
printCheckedGrid(GRID)
print(' ')

def isCorrect(x, y, num):
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


def solve():
    for x in range(len(GRID)):
        for y in range(len(GRID)):
            #print(y,x)
            if GRID[x][y] == 0:
                for num in range(1, 10):
                    if isCorrect(x, y, num):
                        GRID[x][y] = num
                        solve()
                        GRID[x][y] = 0
                return
    print('Solved Sudoku:')
    printCheckedGrid(GRID)



solve()
