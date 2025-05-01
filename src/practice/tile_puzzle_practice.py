# Goal state of the puzzle
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def print_puzzle(state):
    """Print the current state of the puzzle"""
    for row in state:
        print(row)
    print()

def find_blank(state):
    """Find the position of the blank tile (0)"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_possible_moves(state):
    """Get all possible moves from the current state"""
    moves = []
    row, col = find_blank(state)
    
    # Check all four directions
    if row > 0:  # Can move up
        moves.append((row-1, col))
    if row < 2:  # Can move down
        moves.append((row+1, col))
    if col > 0:  # Can move left
        moves.append((row, col-1))
    if col < 2:  # Can move right
        moves.append((row, col+1))
    
    return moves

def make_move(state, move):
    """Make a move by swapping the blank with the specified position"""
    new_state = [row[:] for row in state]  # Create a copy of the state
    blank_row, blank_col = find_blank(state)
    move_row, move_col = move
    
    # Swap the blank with the move position
    new_state[blank_row][blank_col], new_state[move_row][move_col] = \
        new_state[move_row][move_col], new_state[blank_row][blank_col]
    
    return new_state

def count_misplaced_tiles(state):
    """Count how many tiles are not in their goal position"""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

def solve_puzzle(initial_state):
    """Solve the puzzle using a simple breadth-first search"""
    from collections import deque
    
    # Initialize the queue with the initial state and an empty path
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        # Convert state to tuple for hashing
        state_tuple = tuple(tuple(row) for row in current_state)
        
        # Skip if we've seen this state before
        if state_tuple in visited:
            continue
        
        # Mark this state as visited
        visited.add(state_tuple)
        
        # Check if we've reached the goal
        if current_state == goal_state:
            return path
        
        # Get all possible moves
        moves = get_possible_moves(current_state)
        
        # Add new states to the queue
        for move in moves:
            new_state = make_move(current_state, move)
            new_path = path + [move]
            queue.append((new_state, new_path))
    
    return None  # No solution found

# Initial state of the puzzle
initial_state = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

# Solve the puzzle
print("Initial state:")
print_puzzle(initial_state)

solution = solve_puzzle(initial_state)
if solution:
    print("Solution found!")
    print("Number of moves:", len(solution))
    print("Moves:", solution)
    
    # Show each step of the solution
    current_state = [row[:] for row in initial_state]
    for i, move in enumerate(solution, 1):
        current_state = make_move(current_state, move)
        print(f"\nStep {i}:")
        print_puzzle(current_state)
else:
    print("No solution exists!")

                
        

