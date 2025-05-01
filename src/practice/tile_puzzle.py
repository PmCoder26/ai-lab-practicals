import heapq

# Final goal state (like a constant in Java)
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic function (Manhattan Distance)
def calculate_heuristic(state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                total_distance += abs(i - goal_x) + abs(j - goal_y)
    return total_distance

# Find the position of the empty tile (0)
def get_blank_position(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Generate all valid neighboring states
def get_neighbor_states(state):
    blank_row, blank_col = get_blank_position(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []

    for dr, dc in directions:
        new_row = blank_row + dr
        new_col = blank_col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Deep copy of the 2D array (like cloning an array in Java)
            new_state = [row[:] for row in state]
            # Swap blank with the target
            new_state[blank_row][blank_col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)

    return neighbors

# Check if current state is goal
def is_goal(state):
    return state == GOAL_STATE

# A* algorithm implementation
def solve_puzzle(start_state):
    open_list = []  # This is like PriorityQueue<Node>
    g_cost = 0
    h_cost = calculate_heuristic(start_state)
    heapq.heappush(open_list, (g_cost + h_cost, g_cost, start_state))

    # Visited states (like HashMap<String, int[][]>)
    came_from = {tuple(map(tuple, start_state)): None}
    g_scores = {tuple(map(tuple, start_state)): 0}

    while open_list:
        _, current_g, current_state = heapq.heappop(open_list)

        if is_goal(current_state):
            # Reconstruct the path from goal to start
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = came_from[tuple(map(tuple, current_state))]
            return path[::-1]  # Reverse the path

        for neighbor in get_neighbor_states(current_state):
            neighbor_key = tuple(map(tuple, neighbor))
            new_g = current_g + 1

            if neighbor_key not in g_scores or new_g < g_scores[neighbor_key]:
                g_scores[neighbor_key] = new_g
                came_from[neighbor_key] = current_state
                f_cost = new_g + calculate_heuristic(neighbor)
                heapq.heappush(open_list, (f_cost, new_g, neighbor))

    return None  # No solution found

# Main test
if __name__ == "__main__":
    start_state = [
        [1, 2, 3],
        [7, 0, 6],
        [4, 8, 5]
    ]

    solution = solve_puzzle(start_state)

    if solution:
        print("Solution found!")
        for step_index, state in enumerate(solution):
            print(f"\nStep {step_index}:")
            for row in state:
                print(row)
    else:
        print("No solution found.")