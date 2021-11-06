'''
Longest Increasing Subsequence

(Ex: https://leetcode.com/problems/longest-increasing-subsequence/)
'''

from bisect import bisect_left

def lis(nums):
    L = []
    longest_sequences = [[]]
    for num in nums:
        idx = bisect_left(L, num)
        new_sequence = longest_sequences[idx] + [num]
        if idx >= len(L):
            L.append(num)
            #create sequence
            longest_sequences.append(new_sequence)
        else:
            L[idx] = num
            #create sequence
            longest_sequences[idx + 1] = new_sequence
    
    return longest_sequences[-1]

nums = [1, 5, 10, 2, 11, 4, 9, 6, 7, 3]
print(lis(nums))
