'''
Quickselect
time: N + N/2 + N/4 + N/8 + N/16 ... = O(2N) = O(N)
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

def kthSmallest(l, r, k):
    idx = partition(l, r)
    if idx - l == k - 1:
        return nums[idx]
    elif idx - l > k - 1:
        return kthSmallest(l, idx - 1, k)
    else:
        return kthSmallest(idx + 1, r, k - (idx - l + 1))

#Driver code

nums = [10, 4, 5, 8, 6]
n = len(nums)

k = 2 #1-index
print("K-th smallest element is ", end = "")
print(kthSmallest(0, n - 1, k))