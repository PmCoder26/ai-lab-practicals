class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        if self.head is None:
            head = Node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)
        self.size += 1

    def printList(self):
        if self.size == 0:
            print("List is empty!")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data, end=", ")
            print()

    def get(self, idx):
        if self.head is None:
            return -1
        else:
            curr = self.head
            for i in range(0, idx):
                curr = curr.next
            return curr.data


class Graph:

    def __init__(self):
        self.list = [None] * 5
        self.list[0] = LinkedList()

    def dfs(self, visited, ele):
        visited[ele] = True
        print(ele, end=", ")
        curr = self.list[ele]
        for i in range(0, curr.size):
            v = curr.get(i)
            if visited[v]:
                self.dfs(visited, v)
            else:
                continue

    def bfs(self):
