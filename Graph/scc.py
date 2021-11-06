'''
Strongly Connected Component

Step1: do first DFS -> sort the node in order of decreasing finished time (topological sort)
Step2: do second DFS for transposed graph following the topological order
Step: vertices of each tree are strongly connected components

'''

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [[] for _ in range(num)]
        self.transpose = [[] for _ in range(num)]
        self.colors = ['White' for _ in range(num)]
        self.finished_nodes = []
        self.temp_bucket = []
        self.scc = []

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.transpose[b].append(a)

    def topological_sort(self):
        for i in range(self.V):
            if self.colors[i] == 'White':
                self.dfs(i)

    def dfs(self, s, trans=False):
        self.colors[s] = 'Gray'
        graph = self.transpose if trans else self.graph
        if trans:
            self.temp_bucket.append(s)

        for ad in graph[s]:
            if self.colors[ad] == 'White':
                self.dfs(ad, trans)
        self.colors[s] = 'Black'

        if not trans:
            self.finished_nodes.append(s)

    def get_sccs(self):
        self.topological_sort()
        self.colors = ['White' for _ in range(self.V)]
        for i in self.finished_nodes[::-1]:
            if self.colors[i] == 'White':
                self.temp_bucket.clear()
                self.dfs(i, trans=True)
                self.scc.append(self.temp_bucket[:])

g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 5)
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(6, 4)


g.get_sccs()

print(g.finished_nodes)
print(g.scc)




