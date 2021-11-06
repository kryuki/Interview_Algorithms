'''
Recursive version of DFS
'''

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=', ')
    for ad in graph[node]:
        if ad not in visited:
            visited.add(ad)
            dfs(ad)

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

dfs("A")