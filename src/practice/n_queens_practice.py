
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


def is_safe(board, row, col):
    # column check.
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q':
            return False
    
    # left diagonal check.
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    # right diagonal check.
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board[0]):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True


def n_queens(board, row):
    if row == len(board):
        print_board(board)
        print('*****************')   
    else:
        for j in range(len(board[0])):
            if is_safe(board, row, j):
                board[row][j] = 'Q'
                n_queens(board, row + 1)
                board[row][j] = 'X'


n = int(input('Enter the board size: '))
board = [['X' for _ in range(n)] for _ in range(n)]
n_queens(board, 0)
