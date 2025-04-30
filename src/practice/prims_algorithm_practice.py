graph_nodes = {
    'A': [('B', 2), ('C', 1)],
    'B': [('A', 2), ('C', 2), ('D', 5), ('E', 10)],
    'C': [('A', 1), ('B', 2), ('E', 9)],
    'D': [('B', 5), ('F', 8)],
    'E': [('B', 10), ('C', 9)],
    'F': [('D', 8), ('E', 5)]
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
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost


def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i+1, len(list)):
            if list[j].cost < list[min].cost:
                min = j

        list[min], list[i] = list[i], list[min]


def prims_algorithm():
    mst_node_list = [Pair('A', 0)]
    final_cost = 0
    while len(mst_node_list) > 0:
        curr = mst_node_list.pop(0)
        if visited[curr.node] == False:
            visited[curr.node] = True
            final_cost += curr.cost
            for (node, cost) in graph_nodes.get(curr.node):
                mst_node_list.append(Pair(node, cost))
            selection_sort(mst_node_list)
    
    print("The minimum cost of MST is:", final_cost)


prims_algorithm()
    