'''
Created on 2015-7-22

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        i = n - 1
        nret = n
        while i > 0:
            if nums[i - 1] == nums[i]:
                nums.pop(i)
                nret -= 1
            i -= 1
        print(nums)
        return nret
    def removeDuplicates1(self, nums):
        n = len(nums)
        i = n - 1
        nret = n
        while i > 1:
            if nums[i - 2] == nums[i]:
                nums.pop(i)
                nret -= 1
            i -= 1
        print(nums)
        return nret
sl = Solution()
sl.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5])
sl.removeDuplicates1([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5])
            