'''
Dijkstra's algorithm
Single-Source Shortest Path (SSSP)
-edge weights are nonnegative
time: O((V + E)logV)
space: O(V + E)
'''

import math
import heapq

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [[] for _ in range(num)]
        self.dist = [math.inf for _ in range(num)]
    def add_edge(self, a, b, weight):
        self.graph[a].append((b, weight))
    def dijkstra(self, source):
        #initialize
        self.dist[source] = 0
        heap = [(self.dist[i], i) for i in range(self.V)]

        #O(V)
        heapq.heapify(heap)

        #O((V + E)logV)
        while heap:
            cur_dist, u = heapq.heappop(heap)
            for ad, weight in self.graph[u]:
                new_dist = cur_dist + weight
                if new_dist < self.dist[ad]:
                    self.dist[ad] = new_dist
                    heapq.heappush(heap, (new_dist, ad))
        
        return self.dist

#Driver code
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 1, 3)
g.add_edge(3, 2, 9)
g.add_edge(3, 4, 2)
g.add_edge(4, 0, 7)
g.add_edge(4, 2, 6)

g.dijkstra(0)

print(g.dist)