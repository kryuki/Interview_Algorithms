class Heap:
    def __init__(self, nums):
        self.heap = nums
        self.L = len(nums)
        self.build_max_heap()
    #O(N)
    def build_max_heap(self):
        for i in range(self.L - 1, -1, -1):
            self.max_heapify(i, self.L)
    #O(logN)
    def sift_up(self, idx):
        cur = idx
        while cur != 0 and self.heap[cur] > self.heap[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)
    #O(logN)
    def max_heapify(self, idx, end_idx):
        l, r = idx * 2 + 1, idx * 2 + 2
        largest = idx
        lst = self.heap
        if l < end_idx and lst[l] > lst[idx]:
            largest = l
        if r < end_idx and lst[r] > lst[largest]:
            largest = r
        if largest != idx:
            self.swap(idx, largest)
            self.max_heapify(largest, end_idx)
    def heapsort(self):
        for end_idx in range(self.L - 1, 0, -1):
            self.swap(0, end_idx)
            self.max_heapify(0, end_idx)
            end_idx -= 1
        return self.heap
    def parent(self, idx):
        return (idx - 1) // 2
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

#time: Best-O(NlogN), Worst-O(NlogN), Average-O(NlogN)
#space: O(1)(ideal)
nums = [-7, 10, 5, 3, 4, 8, 1, 6]
heap = Heap(nums)
print(heap.heapsort())