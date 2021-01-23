emptyGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

''' 
emptyGrid = [[0, 0, 4, 0, 7, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 7, 5], [0, 0, 0, 0, 0, 0, 8, 0, 9],
             [0, 0, 0, 0, 6, 3, 0, 9, 0], [6, 0, 0, 0, 9, 0, 0, 0, 1], [0, 2, 0, 8, 4, 0, 0, 0, 0],
             [5, 0, 7, 0, 0, 0, 0, 0, 0], [3, 4, 0, 0, 0, 8, 7, 0, 0], [0, 0, 0, 0, 2, 0, 9, 0, 0]]


emptyGrid = [[7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
'''


def printGrid(grid):  # checks whether the board is correct (9x9 grid)
    counterX = 0
    counterY = 0
    for i in range(len(grid)):
        counterX += 1
        for j in range(len(grid[i])):
            counterY += 1

    if counterX == 9 and counterY == 81:
        return printCheckedGrid(grid)
    else:
        print('ERROR! Wrong size of sudoku!')
        return False


def printCheckedGrid(grid):  # if grid is 9x9 (correct sudoku board) then prints it
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")
    return grid

#print(findEmpty(emptyGrid))

#print(solve(printGrid(emptyGrid)))
