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
    def __init__(self, parent, node, cost):
        self.node = node     
        self.parent = parent   
        self.cost = cost


def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i+1, len(list)):
            if list[j].cost < list[min].cost:
                min = j

        list[min], list[i] = list[i], list[min]


def prims_algorithm():
    mst_node_list = [Pair(None, 'A', 0)]
    tree_list = []
    final_cost = 0
    while len(mst_node_list) > 0:
        curr = mst_node_list.pop(0)
        if visited[curr.node] == False:
            visited[curr.node] = True
            final_cost += curr.cost
            tree_list.append(curr)
            for (node, cost) in graph_nodes.get(curr.node):
                if visited[node] == False:
                    mst_node_list.append(Pair(curr.node, node, cost))
            selection_sort(mst_node_list)
    
    for edge in tree_list:
        print(edge.parent, '--', edge.cost, '--', edge.node)
    print("The minimum cost of MST is:", final_cost)


prims_algorithm()
    