n = int(input('Enter N: ')) 
board = [[0] * n for _ in range(n)]

def print_res(board):
    for row in board:
        print(*row)
    print('--------------------------------------------')
def safe(board, i, j):
    if 1 in board[i]:
        return False
    i1, j1 = i - 1, j - 1
    while i1 > -1 and j1 > -1: 
        if board[i1][j1] == 1:
           return False
        i1 -= 1
        j1 -= 1 
    n = len(board)
    i2, j2 = i + 1, j - 1
    while i2 < n and j2 < n:
        if board[i2][j2] == 1:
            return False
        i2 += 1
        j2 -= 1
    return True


def nQueens(n, board, col=0):
    if col == n:
        print_res(board)
        return

    for row in range(n):
        if safe(board, row, col):
            board[row][col] = 1
            nQueens(n, board, col + 1)
        board[row][col] = 0

nQueens(n, board)


""""
output:

Enter N: 4
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0
--------------------------------------------
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
--------------------------------------------
"""

