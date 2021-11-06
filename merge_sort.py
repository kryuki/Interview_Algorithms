import math

def merge_sort(nums):
    ms_helper(nums, 0, len(nums) - 1)

def ms_helper(nums, l, r):
	if l >= r:
		return
	mid = (l + r) // 2
	ms_helper(nums, l, mid)
	ms_helper(nums, mid + 1, r)
	merge(nums, l, mid, r)

def merge(nums, l, mid, r):
    L = nums[l : (mid + 1)] + [math.inf]
    R = nums[(mid + 1) : (r + 1)] + [math.inf]
    #combine L & R
    idx_l, idx_r = 0, 0
    for i in range(l, r + 1):
        if L[idx_l] <= R[idx_r]:
            nums[i] = L[idx_l]
            idx_l += 1
        else:
            nums[i] = R[idx_r]
            idx_r += 1
    
#time: Best-O(NlogN), Worst-O(NlogN), Average-O(NlogN)
#space: O(N)
nums = [-7, 10, 5, 3, 4, 8, 1, 6]
merge_sort(nums)
print(nums)