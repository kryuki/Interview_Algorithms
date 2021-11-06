'''
The Bellman-Ford algorithm
Single-Source Shortest Path (SSSP)
-edge weights may be negative
-can detect negative weight cycle
time: O(VE)
space: O(V + E)
'''

import math

class Graph:
    def __init__(self, num):
        self.V = num
        self.dist = [math.inf for _ in range(num)]
        self.edges = []
        self.parent = [None for _ in range(num)]
    
    def add_edge(self, a, b, w):
        self.edges.append((a, b, w))

    def bellman_ford(self, s):
        self.dist[s] = 0
        for _ in range(self.V - 1):
            for a, b, w in self.edges:
                #Relax
                if self.dist[a] + w < self.dist[b]:
                    self.dist[b] = self.dist[a] + w
                    self.parent[b] = a
    
    def contain_negative_weight_cycle(self):
        for a, b, w in self.edges:
            if self.dist[b] > self.dist[a] + w:
                return True
        return False

#Driver code
g = Graph(5)
g.add_edge(0, 1, 6)
g.add_edge(0, 3, 7)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, -4)
g.add_edge(2, 1, -2)
g.add_edge(3, 2, -3)
g.add_edge(4, 0, 2)
g.add_edge(4, 2, 7)

g.bellman_ford(0)

print(g.dist)
print(g.contain_negative_weight_cycle())