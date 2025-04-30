graph_nodes = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('C', 11), ('D', 9)],
    'C': [('A', 5), ('B', 11), ('E', 3)],
    'D': [('B', 9), ('E', 7), ('F', 2)],
    'E': [('C', 3), ('D', 7), ('F', 6)],
    'F': [('D', 2), ('E', 6)]
}

visited = {
    'A': False,
    'B': False,
    'C': False,
    'D': False,
    'E': False,
    'F': False
}


