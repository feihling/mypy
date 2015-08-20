'''
Created on 2015-7-22

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement1(self, nums, val):
        n = len(nums)
        i = n - 1
        ret_num = n
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
                ret_num -= 1
            i -= 1
        return ret_num
    
    def removeElement(self, nums, val):
        n = len(nums)
        i = n - 1
        ret_num = n
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
                ret_num -= 1
            i -= 1
        return ret_num

sl = Solution()
print(sl.removeElement([3,3], 3))