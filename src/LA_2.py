# Prim's Minimal Spanning Tree Algorithm
# Dijkstra's Minimal Spanning Tree Algorithm


class Pair:
    def __init__(self, src, cost):
        self.src = src
        self.cost = cost

class GraphEdge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, edge):
        newNode = ListNode(edge)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
        self.size += 1

    def printList(self):
        curr = self.head
        while curr is not None:
            print("src:", curr.src, "dest:", curr.dest, "weight:", curr.weight)
            curr = curr.next

    def get(self, idx):
        curr = self.head
        for i in range(0, idx):
            curr = curr.next
        return curr.data


class Graph:

    def __init__(self):
        self.list = [None] * 6

        self.list[0] = List()
        self.list[0].add(GraphEdge(0, 1, 2))
        self.list[0].add(GraphEdge(0, 2, 1))

        self.list[1] = List()
        self.list[1].add(GraphEdge(1, 0, 2))
        self.list[1].add(GraphEdge(1, 2, 2))
        self.list[1].add(GraphEdge(1, 3, 5))
        self.list[1].add(GraphEdge(1, 4, 10))

        self.list[2] = List()
        self.list[2].add(GraphEdge(2, 0, 1))
        self.list[2].add(GraphEdge(2, 1, 2))
        self.list[2].add(GraphEdge(2, 4, 9))

        self.list[3] = List()
        self.list[3].add(GraphEdge(3, 1, 5))
        self.list[3].add(GraphEdge(3, 5, 8))

        self.list[4] = List()
        self.list[4].add(GraphEdge(4, 1, 10))
        self.list[4].add(GraphEdge(4, 2, 9))
        self.list[4].add(GraphEdge(4, 5, 5))

        self.list[5] = List()
        self.list[5].add(GraphEdge(5, 3, 8))
        self.list[5].add(GraphEdge(5, 4, 5))

    def __selectionSort(self, mstList):
        for i in range(0, len(mstList) - 1):
            min = i
            for j in range(i + 1, len(mstList)):
                if mstList[j].cost < mstList[min].cost:
                    min = j
            temp = mstList[i]
            mstList[i] = mstList[min]
            mstList[min] = temp

    def primsAlgo(self):
        mstList = []
        visited = [False] * 6
        mstList.append(Pair(0, 0))
        finalCost = 0
        while len(mstList) != 0:
            curr = mstList.pop(0)
            if visited[curr.src] == False:
                visited[curr.src] = True
                finalCost += curr.cost
                for i in range(0, self.list[curr.src].size):
                    edge = self.list[curr.src].get(i)
                    mstList.append(Pair(edge.dest, edge.weight))
                self.__selectionSort(mstList)
        print("The minimum cost of MST is:", finalCost)


# -------------------------------------------------------------------------------------------------------------->

graph = Graph()
graph.primsAlgo()