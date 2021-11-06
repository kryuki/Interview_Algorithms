'''
Prim's algorithm
Minimum Spanning Tree (MST)
time: O(ElogE)
'''

class Node:
    def __init__(self, idx, val, parent=None):
        self.idx = idx
        self.val = val
        self.parent = None
    def __lt__(self, other):
        return self.val < other.val
    def __eq__(self, other):
        return self.val == other.val

class Heap:
    def __init__(self, node_nums):
        self.heap = node_nums
        self.L = len(node_nums)
        self.map = {i : i for i in range(self.L)}
        self.build_min_heap()
    def heap_push(self, val):
        new_node = Node(self.L, val)
        self.map[self.L] = self.L
        self.heap.append(new_node)
        self.L += 1
        self.sift_up(self.L - 1)
    def heap_pop(self):
        res = self.heap[0]
        self.swap(0, self.L - 1)
        self.map.pop(res.idx)
        self.heap.pop()
        self.L -= 1
        self.min_heapify(0, self.L)
        return res
    def build_min_heap(self):
        for i in range(self.L - 1, -1, -1):
            self.min_heapify(i, self.L)
    def sift_up(self, idx):
        cur = idx
        while cur != 0 and self.heap[cur] < self.heap[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)
    def min_heapify(self, idx, end_idx):
        lst = self.heap
        l, r = idx * 2 + 1, idx * 2 + 2
        largest = idx
        if l < end_idx and lst[l] < lst[idx]:
            largest = l
        if r < end_idx and lst[r] < lst[largest]:
            largest = r
        if largest != idx:
            self.swap(idx, largest)
            self.min_heapify(largest, end_idx)
    def decrease_key(self, idx, key):
        idx = self.map[idx]
        key_node = self.heap[idx]
        key_node.val = key
        self.sift_up(idx)
    def insert_key(self, key):
        self.L += 1
        self.heap.append(key)
        self.sift_up(self.map[self.L - 1])
    def parent(self, idx):
        return (idx - 1) // 2
    def swap(self, idx1, idx2):
        node1, node2 = self.heap[idx1], self.heap[idx2]
        self.map[node1.idx], self.map[node2.idx] = self.map[node2.idx], self.map[node1.idx]
        self.heap[idx1], self.heap[idx2] = node2, node1
    def show(self):
        for node in self.heap:
            print(node.val, end=' ')
        print()

import math
class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [[] for _ in range(num)]
        self.parent = [None for _ in range(num)]
        self.heap = Heap([Node(idx, math.inf) for idx in range(num)])
        self.summ = 0
    
    def add_edge(self, a, b, weight):
        self.graph[a].append((b, weight))
        self.graph[b].append((a, weight))
    
    def prims_algorithm(self, s):
        #initialize
        self.heap.decrease_key(0, 0)
        visited = set()
        cnt = 0
        while self.heap.heap:
            print(cnt)
            cur_node = self.heap.heap_pop()
            u = cur_node.idx
            self.summ += cur_node.val
            visited.add(u)
            for ad, weight in self.graph[u]:
                if ad in visited:
                    continue
                ad_node_idx = self.heap.map[ad]
                ad_node = self.heap.heap[ad_node_idx]
                if weight < ad_node.val:
                    self.parent[ad] = u
                    self.heap.decrease_key(ad_node.idx, weight)
            cnt += 1


#Driver code
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 8)
g.add_edge(1, 6, 11)
g.add_edge(1, 2, 8)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 4)
g.add_edge(2, 5, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 8, 14)
g.add_edge(4, 8, 10)
g.add_edge(5, 6, 7)
g.add_edge(5, 7, 6)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 2)

g.prims_algorithm(0)

print(g.parent)
print(g.summ)