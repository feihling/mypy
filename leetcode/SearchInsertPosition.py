'''
Created on 2015-7-29

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert1(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i + 1

    def searchInsert(self, nums, target):
        n = len(target)
        media = n / 2

sl = Solution()
print(sl.searchInsert([1,3,5,6], 5))
print(sl.searchInsert([1,3,5,6], 7))
print(sl.searchInsert([1,3,5,6], 0))