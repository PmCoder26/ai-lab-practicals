class GraphNode:
    def __init__(self, data):
        self.data = data


class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class List:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        newNode = ListNode(data)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode
        self.size += 1

    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=", ")
            curr = curr.next
        print()

    def get(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr.data


class Graph:

    def __init__(self):
        self.list = [None] * 5
        self.list[0] = List()
        self.list[0].add(1)
        self.list[0].add(2)

        self.list[1] = List()
        self.list[1].add(0)
        self.list[1].add(3)
        self.list[1].add(4)

        self.list[2] = List()
        self.list[2].add(0)
        self.list[2].add(3)
        self.list[2].add(4)

        self.list[3] = List()
        self.list[3].add(1)
        self.list[3].add(2)
        self.list[3].add(4)

        self.list[4] = List()
        self.list[4].add(1)
        self.list[4].add(2)
        self.list[4].add(3)

    def dfs(self, visited, idx):
        visited[idx] = True
        print(idx, end=", ")
        curr = self.list[idx]
        for i in range(0, curr.size):
            v = curr.get(i)
            if visited[v] == False:
                self.dfs(visited, v)
            else:
                continue

    def bfs(self):
        nodeQueue = []
        visited = [False] * 5
        nodeQueue.append(0)
        while len(nodeQueue) != 0:
            curr = nodeQueue[0]
            nodeQueue.pop(0)
            if visited[curr] == False:
                visited[curr] = True
                print(curr, end=", ")
            temp = self.list[curr]
            for i in range(0, temp.size):
                if visited[temp.get(i)] == False:
                    nodeQueue.append(temp.get(i))
                else:
                    continue
        print()


# ---------------------------------------------------------------------------->

graph = Graph()
visited = [False] * 5

print("The DFS traversal of the graph is:")
graph.dfs(visited, 0)
print()

print("The BFS traversal of the graph is:")
graph.bfs()