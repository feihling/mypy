'''
Created on 2015-7-28

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        n = len(nums)
        i = 0
        j = n - 1
        num_0 = 0
        while i <= j:
            if nums[i] == 0:
                nums[i] = nums[num_0]
                nums[num_0] = 0
                num_0 += 1
            elif nums[i] == 2:
                nums[i] = nums[j]
                nums[j] = 2
                j -= 1
                i -= 1
            i += 1
        print(nums)

sl = Solution()
sl.sortColors([0, 1, 2, 0, 1, 2])
sl.sortColors([1, 1, 2, 0, 1, 2])
sl.sortColors([2, 1, 2, 0, 1, 2])