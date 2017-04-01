__author__ = 'Arman Malekzade'
import Queue

class Graph:

    def __init__(self, adj):
        self.adj_list = adj

    def bfs(self, root):
        print '-------------------------------'
        visited = []
        for i in range(len(adj_list)):
            visited.append(False)
        q = Queue.LifoQueue()
        visited[root] = True
        q.put(root)
        while not q.empty():  # O(V)
            current = q.get()
            print current, '\n'
            current_adj = adj_list[current]
            for v in current_adj:
                if not visited[v]:
                    visited[v] = True
                    q.put(v)
        print '-------------------------------'

    def dfs(self, root):
        print '-------------------------------'
        visited = []
        for i in range(len(adj_list)):
            visited.append(False)
        Stack = []
        visited[root] = True
        Stack.append(root)
        while Stack:
            current = Stack.pop()
            print current, '\n'
            current_adj = adj_list[current]
            for v in current_adj:
                if not visited[v]:
                    visited[v] = True
                    Stack.append(v)
        print '-------------------------------'

adj_list = [
    [1],
    [1, 2, 3],
    [0, 3],
    [2]
]

g = Graph(adj_list)
g.bfs(2)
g.dfs(3)
