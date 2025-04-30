graph_nodes = {
    'A': ['E', 'C', 'B'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'F', 'D', 'B'],
    'D': ['B', 'C', 'F'],
    'E': ['A', 'F'],
    'F': ['E', 'C', 'D']
}

visited = {
    'A': False,
    'B': False,
    'C': False,
    'D': False,
    'E': False,
    'F': False
}


def bfs(src):
    list = [src]
    while len(list) > 0:
        ele = list.pop(0)
        if visited.get(ele) == False:
            visited[ele] = True
            print(ele, end=' ')
            temp = graph_nodes.get(ele)
            for n in temp:
                list.append(n)
    print()

def dfs(src):
    print(src, end=' ')
    visited[src] = True
    for node in graph_nodes.get(src):
        if visited.get(node) == False:
            dfs(node)
        else:
            continue


dfs('A')
print()