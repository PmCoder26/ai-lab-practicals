# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

# Function to check if a player has won
def is_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to return a list of empty positions
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Function to evaluate the board state
def evaluate(board):
    if is_winner(board, 'X'):
        return 1   # AI wins
    elif is_winner(board, 'O'):
        return -1  # Human wins
    else:
        return 0   # Draw

# Minimax algorithm (recursive) to evaluate best score
def minimax(board, is_maximizing):
    if is_winner(board, 'X') or is_winner(board, 'O') or is_full(board):
        return evaluate(board)

    if is_maximizing:  # AI's turn
        best_score = float('-inf')
        for i, j in get_available_moves(board):
            board[i][j] = 'X'
            score = minimax(board, False)
            board[i][j] = ' '
            best_score = max(best_score, score)
        return best_score
    else:  # Human's turn
        best_score = float('inf')
        for i, j in get_available_moves(board):
            board[i][j] = 'O'
            score = minimax(board, True)
            board[i][j] = ' '
            best_score = min(best_score, score)
        return best_score

# Function to choose the best move for AI (similar to A* approach)
def get_best_move(board, player):
    best_score = float('-inf') if player == 'X' else float('inf')
    best_move = None

    for i, j in get_available_moves(board):
        board[i][j] = player
        score = minimax(board, is_maximizing=(player == 'O'))
        board[i][j] = ' '

        if player == 'X' and score > best_score:
            best_score = score
            best_move = (i, j)
        elif player == 'O' and score < best_score:
            best_score = score
            best_move = (i, j)

    return best_move
 
# Main function to run the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!\nYou are O, AI is X.")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell already taken!")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column between 0 and 2.")

        print("\nYour move:")
        print_board(board)

        if is_winner(board, 'O'):
            print("🎉 You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("\nAI is thinking...")
        ai_move = get_best_move(board, 'X')
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'X'

        print("\nAI's move:")
        print_board(board)

        if is_winner(board, 'X'):
            print("💻 AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
play_game()