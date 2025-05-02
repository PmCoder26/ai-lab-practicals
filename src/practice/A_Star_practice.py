Graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 0)]
}

h_values = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0
}


def get_neighbors(n):
    return Graph.get(n)

def get_h(n):
    return h_values.get(n)


def a_star(start, end):
    open_set = set(start)
    closed_set = set()
    parents = {}
    g = {}
    
    g[start] = 0
    parents[start] = start

    while len(open_set) > 0:
        n = None

        # getting the node of shortest cost.
        for v in open_set:
            if n == None or g.get(v) + get_h(v) < g.get(n) + get_h(n):
                n = v

        # if n is None that means no path exists.
        if n is None:
            print("Path doesn't exists!")
            return n
        
        # if n is end node then simple return the path.
        if n == end:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print('The required path is:', path)
            return path
        
        # now extracting the neighbouring nodes.
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[n] + weight < g[m]:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)
    
    print("Path doesn't exists.")
    return None

a_star('S', 'D')