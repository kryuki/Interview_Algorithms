'''
Non-recursive version of DFS
'''

visited = set()
stack = []

def DFS_nonrecursive(s):
    visited.add(s)
    stack.append(s)
    while stack:
        u = stack.pop()
        print(u, end=' ,')
        for ad in graph[u]:
            if ad not in visited:
                visited.add(ad)
                stack.append(ad)

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

DFS_nonrecursive("A")