'''
Kruskal's algorithm
Minimum Spanning Tree (MST)
time: O(ElogE)
'''

class UnionFind:
    def __init__(self, num):
        self.V = num
        self.parents = list(range(num))
        self.ranks = [0 for _ in range(num)]

    def find_set(self, u):
        parents = self.parents
        if u != parents[u]:
            parents[u] = self.find_set(parents[u])
        return parents[u]
    
    def union(self, set1, set2):
        if set1 == set2:
            return
        rank1, rank2 = self.ranks[set1], self.ranks[set2]
        if rank1 > rank2:
            self.parents[set2] = set1
        else:
            self.parents[set1] = set2
            if rank1 == rank2:
                self.ranks[set2] += 1

class Graph:
    def __init__(self, num):
        self.V = num
        self.edges = []
        self.uf = UnionFind(num)
    
    def add_edge(self, a, b, w):
        self.edges.append((a, b, w))
    #ElogE
    def kruskal(self):
        #sort the edges into nondecreasing order
        self.edges.sort(key=lambda x:x[2])
        connected_cnt = 0
        connected_weight = 0
        #O(E) * find_set operations
        #O(V) * union operations
        #-> O(E + V)α(V), where α is the very slowly growing function
        for a, b, w in self.edges:
            if self.uf.find_set(a) != self.uf.find_set(b):
                self.uf.union(self.uf.find_set(a), self.uf.find_set(b))
                print("add:", a, b, w)
                connected_weight += w
                connected_cnt += 1
            if connected_cnt == self.V - 1:
                break
        return connected_weight

#Driver code

g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 8, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

print(g.kruskal())
