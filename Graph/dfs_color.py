'''
DFS algorithm using colors
'White': unvisited
'Gray': visiting
'Black': visited
'''

class Graph:
    def __init__(self, num):
        self.graph = [[] for _ in range(num)]
        self.colors = ['White' for _ in range(num)]
        self.parents = list(range(num))
        self.discovered_time = [0 for _ in range(num)]
        self.finished_time = [0 for _ in range(num)]
        self.global_time = 0
    
    def add_edge(self, a, b):
        self.graph[a].append(b)
    
    def dfs(self, u):
        self.global_time += 1
        print(idx_to_node_dict[u], end=' ,')

        #start exploring
        self.discovered_time[u] = self.global_time
        self.colors[u] = "Gray"
        for ad in self.graph[u]:
            if self.colors[ad] == "White":
                self.parents[ad] = u
                self.dfs(ad)
        
        #finish exploring
        self.colors[u] = "Black"
        self.global_time += 1
        self.finished_time[u] = self.global_time

#Driver code
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

'''
　　　　　　A
         ↙　　↘
        B      C
    　↙   ↘     ↘
     D     E  ->  F
'''
nodes = list(graph.keys())
node_to_idx_dict = {node : idx for idx, node in enumerate(nodes)}
idx_to_node_dict = {idx : node for idx, node in enumerate(nodes)}

#construct graph
V = len(nodes)
g = Graph(V)
for node in nodes:
    for ad in graph[node]:
        g.add_edge(node_to_idx_dict[node], node_to_idx_dict[ad])

for node in nodes:
    s = node_to_idx_dict[node]
    if g.colors[s] == 'White':
        g.dfs(s)
print()
print(g.discovered_time)
print(g.finished_time)