'''
Created on 2015-6-19

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        tmp1 = [nums[0]]
        tmp2 = [nums[0]]
        tmp3 = [nums[0]]
        m = len(nums)
        for i in range(1, m):
            tmp1.append(max(nums[i], tmp1[i - 1] * nums[i], tmp2[i - 1] * nums[i]))
            tmp2.append(min(nums[i], tmp1[i - 1] * nums[i], tmp2[i - 1] * nums[i]))
            tmp3.append(max(tmp3[i - 1], tmp1[i]))
        print tmp1
        print tmp2
        print tmp3
sl = Solution()
sl.maxProduct([2,-5,-2,-4,3])