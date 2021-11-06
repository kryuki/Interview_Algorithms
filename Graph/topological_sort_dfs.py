'''
Topological Sort
time: O(V + E)

Step1: call DFS to compute finishing times for each node
Step2: reverse the order of the finished_nodes
'''


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [[] for _ in range(num)]
        self.colors = ['White' for _ in range(num)]
        self.finished_nodes = []
    
    def add_edge(self, a, b):
        self.graph[a].append(b)
    
    def dfs(self, s):
        self.colors[s] = 'Gray'
        for ad in self.graph[s]:
            if self.colors[ad] == 'White':
                self.dfs(ad)
            elif self.colors[ad] == 'Gray':
                self.cycle = True
        self.colors[s] = 'Black'
        self.finished_nodes.append(s)

    def topological_sort(self):
        for i in range(self.V):
            if self.colors[i] == 'White':
                self.dfs(i)


#Driver code

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()
print(g.finished_nodes[::-1])