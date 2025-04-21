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


def get_neighbours(n):
    return Graph.get(n)


def get_h(n):
    return h_values.get(n)


def a_star(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}

    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if (n is None) or (g.get(v) + get_h(v) < g[n] + get_h(n)):
                n = v

        if n is None:
            print("Path doesn't exists.")
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("The required path is: ", path)
            return path

        for (m, weight) in get_neighbours(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
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