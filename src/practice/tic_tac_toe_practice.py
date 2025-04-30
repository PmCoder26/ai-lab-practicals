def print_board(board):
    for row in board:
        print(' | '.join(row))


def is_winner(board, player):
    # row check.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    
    # column check.
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    
    # diagonal check.
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def get_available_moves(board):
    list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                list.append((i, j))
    return list


def evaluate(board):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    return 0


def minimax(board, is_max):
    if is_winner(board, 'X') or is_winner(board, 'O') or is_full(board):
        return evaluate(board)
    
    if is_max:  # for AI's turn(max).
        best_score = float('-inf')
        for (i, j) in get_available_moves(board):
            board[i][j] = 'X'
            score = minimax(board, False)
            board[i][j] = ' '
            best_score = max(best_score, score)
        return best_score
    else:   # for Human's turn(min).
        best_score = float('inf')
        for (i, j) in get_available_moves(board):
            board[i][j] = 'O'
            score = minimax(board, True)
            board[i][j] = ' '
            best_score = min(best_score, score)
        return best_score
    

def get_best_move(board, player):
    best_score = float('-inf') if player == 'X' else float('inf')
    best_move = None

    for (i, j) in get_available_moves(board):
        board[i][j] = player
        score = minimax(board, player == 'O')
        board[i][j] = ' '
        
        if player == 'X' and score > best_score or player == 'O' and score < best_score:
            best_score = score
            best_move = (i, j)        

    return best_move


def start_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print(board)
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and AI is 'X")
    print_board(board)

    while True:
        while True:
            row = int(input('Enter the row(0-2): '))
            col = int(input('Enter the col(0-2): '))
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Cell is already occupied! Try again with different one.")
        
        print("\nYour move!")
        print_board(board)

        if is_winner(board, 'O'):
            print("You won!!!")
            break
        if is_full(board):
            print("Its a tie!!!")
            break

        print("AI's move!")
        ai_move = get_best_move(board, 'X')
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        if is_winner(board, 'X'):
            print('AI wins!!!')
            break
        if is_full(board):
            print("Its a tie!!!")
            break

start_game()



