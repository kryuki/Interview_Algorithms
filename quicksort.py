'''
Quicksort
time: Best-O(NlogN), Worst-O(N^2), Average-O(NlogN)
space: Best-O(logN), Worst-O(N), Average-O(logN)
'''
def swap(i, j):
    nums[i], nums[j] = nums[j], nums[i]

def partition(l, r):
    pivot_val = nums[r]
    end_of_smaller_idx = l - 1
    
    for i in range(l, r):
        if nums[i] <= pivot_val:
            swap(end_of_smaller_idx + 1, i)
            end_of_smaller_idx += 1

    swap(end_of_smaller_idx + 1, r)
    return end_of_smaller_idx + 1

def quickSort(l, r):
    if l < r:
        pivot_idx = partition(l, r)
        quickSort(l, pivot_idx - 1)
        quickSort(pivot_idx + 1, r)

nums = [10, 7, 8, 9, 1, 5, -1, 0, 0, 2, 5, 2, 5]
n = len(nums)
quickSort(0, n - 1)
print(nums)