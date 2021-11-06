'''
The Floyd-Warshall algorithm
All-Pairs Shortest Paths
-edge weights may be negative
-assume there are no negative-weight cycle
time: O(V^3)
'''

import math

class Graph:
    def __init__(self, num):
        self.V = num
        self.dist = [[math.inf for _ in range(num)] for _ in range(num)]
        for i in range(num):
            self.dist[i][i] = 0
        self.parent = [[None for _ in range(num)] for _ in range(num)]

    def add_edge(self, a, b, w):
        self.dist[a][b] = w
        self.parent[a][b] = a

    def floyd_warshall(self):
        for k in range(self.V): #intermediate node
            for i in range(self.V): #start node
                for j in range(self.V): #end node
                    #Relax
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.parent[i][j] = self.parent[k][j]

#Driver code          
N = 5
edges = [(0, 1, 3), 
         (0, 2, 8),
         (0, 4, -4),
         (1, 3, 1),
         (1, 4, 7),
         (2, 1, 4),
         (3, 0, 2),
         (3, 2, -5),
         (4, 3, 6)]

g = Graph(N)
for a, b, w in edges:
    g.add_edge(a, b, w)

g.floyd_warshall()

for i in range(N):
    print(g.dist[i])
for i in range(N):
    print(g.parent[i])

