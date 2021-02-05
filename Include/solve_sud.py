from Include.board import printCheckedGrid as pgrid

def findNextCellToFill(grid, i, j):  # finds empty cell to be filled, when all is filled, returns -1
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isCorrect(grid, i, j, num):  # check whether proposed solution is correct (returns true), returns bool false,
    # when is not
    row = all([num != grid[i][x] for x in range(9)])
    if row:
        col = all([num != grid[x][j] for x in range(9)])
        if col:
            startX = 3 * (i // 3)
            startY = 3 * (j // 3)
            for x in range(startX, startX + 3):
                for y in range(startY, startY + 3):
                    if grid[x][y] == num:
                        return False
            return True
    return False


def solve(grid, i=0, j=0):  # solves sudoku
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True  # finishes when sudoku is filled
    for num in range(1, 10):
        if isCorrect(grid, i, j, num):
            grid[i][j] = num
            if solve(grid, i, j):
                return True
            # undoes current cell to backtrack
            grid[i][j] = 0
    return False

def printSolGrid(grid):
    print('Solved Sudoku: ')
    pgrid(grid)
