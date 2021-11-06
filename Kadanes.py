'''
Kadane's algorithm
(ex: https://www.interviewbit.com/problems/max-sum-contiguous-subarray/)
Point: get the maximum sum of contiguous subarray

Step1: worst maximum is just getting the first value (=nums[0])
Step2: for each element, add the value. If the sum is negative, 
       it's better to throw previous sums away and reset it to 0.
       If the sum is positive, keep the value.
'''

def max_subarray_sum(nums):
    max_so_far = nums[0]
    max_ending_here = 0
    for num in nums:
        max_ending_here += num
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(max_ending_here, 0)
    return max_so_far


#Driver code
nums = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(nums)) #maximum subarray is [4, -1, -2, 1, 5]