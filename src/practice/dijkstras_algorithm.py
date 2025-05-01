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


class Pair:
    def __init__(self, node, path):
        self.node = node
        self.path = path


def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j].path < list[min_index].path:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

def dijkstras_algorithm(src):
    distance = {
        'A': 0.0,
        'B': float('inf'),
        'C': float('inf'),
        'D': float('inf'),
        'E': float('inf'),
        'F': float('inf')
    }

    node_list = [Pair(src, 0.0)]
    while len(node_list) > 0:
        curr = node_list.pop(0)
        if visited[curr.node] == False:
            visited[curr.node] = True
            for (neighbor, weight) in graph_nodes[curr.node]:
                if distance[curr.node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[curr.node] + weight
                    node_list.append(Pair(neighbor, distance[neighbor]))
                    selection_sort(node_list)
    
    for (node, dist) in distance.items():
        print(f"Distance from {src} to {node} is {dist}")

    
dijkstras_algorithm('A')







