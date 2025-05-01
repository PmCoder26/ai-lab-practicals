graph_nodes = {
    'A': [('B', 4), ('C', 5)],
    'B': [('C', 11), ('D', 9)],
    'C': [('E', 3)],
    'D': [('E', 7), ('F', 2)],
    'E': [('F', 6)]
}

parents = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F'
}

ranks = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0
}


class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


def selection_sort(list):
    for i in range(len(list) - 1):
        minIdx = i
        for j in range(i + 1, len(list)):
            if list[j].wt < list[minIdx].wt:
                minIdx = j
        list[i], list[minIdx] = list[minIdx], list[i]



def find(node):
    if parents[node] != node:
        return find(parents[node])  # Path compression
    return parents[node]


def union(src, dest):
    src_parent = find(src)
    dest_parent = find(dest)

    if ranks[src_parent] == ranks[dest_parent]:
        ranks[src_parent] += 1
        parents[dest_parent] = src_parent
    elif ranks[src_parent] < ranks[dest_parent]:
        parents[src_parent] = dest_parent
    else:
        parents[dest_parent] = src_parent


def kruskals_algorithm(src):
    edge_list = []
    final_cost = 0
    i = 0
    count = 0

    for key in graph_nodes.keys():
        for (dest, wt) in graph_nodes.get(key):
            edge_list.append(Edge(key, dest, wt))   
    selection_sort(edge_list)

    for edge in edge_list:
        print('src: ', edge.src, ', weight:', edge.wt, ', dest:', edge.dest)

    while(count < 5):
        curr = edge_list[i]
        src_parent = find(curr.src)
        dest_parent = find(curr.dest)
        print('For ', 'src:', curr.src, ', dest:', dest)

        if src_parent != dest_parent:
            union(curr.src, curr.dest)            
            final_cost += curr.wt
            count += 1                    
        print('Parents:', parents)
        print('Ranks:', ranks)
        print()
        i += 1

    print('The final cost is:', final_cost)
    print('The parents are:', parents)
    print('The ranks are:', ranks)


kruskals_algorithm('A')

