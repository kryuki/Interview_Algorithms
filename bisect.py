class MyBisect:
    def bisect(self, nums, val): #Alias for bisect_left
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= val:
                r = mid
            else:
                l = mid + 1
        return l
    
    def bisect_right(self, nums, val):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > val:
                r = mid
            else:
                l = mid + 1
        return l

#Driver code
nums = [1, 2, 3, 3, 3, 5, 10, 11, 13]
b = MyBisect()
idx1 = b.bisect(nums, 6) #6
idx2 = b.bisect(nums, 3) #2
idx3 = b.bisect(nums, 15) #9
idx4 = b.bisect(nums, 0) #0
print(idx1, idx2, idx3, idx4)

idx5 = b.bisect_right(nums, 6) #6
idx6 = b.bisect_right(nums, 3) #5
idx7 = b.bisect_right(nums, 15) #9
idx8 = b.bisect_right(nums, 0) #0
print(idx5, idx6, idx7, idx8)