from queue import Queue

visited = set()
queue = Queue()

def BFS(s):
    visited.add(s)
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        print(u + ', ', end='')
        for ad in graph[u]:
            if ad not in visited:
                visited.add(ad)
                queue.put(ad)

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

BFS("A")