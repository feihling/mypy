'''
Created on 2015-6-18

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob1(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        tmp = []
        tmp.append(nums[0])
        tmp.append(max(nums[0], nums[1]))
        l = len(nums)
        for i in range(2, l):
            tmp.append(max(nums[i] + tmp[i - 2], tmp[i - 1]))
        print tmp
        return tmp[l - 1]

    def rob(self, nums):
        if len(nums) == 0:
            return 0
        maxSum = nums[0]
        lastSum = 0
        l = len(nums)
        for i in range(1, l):
            tmp = maxSum
            maxSum = max(maxSum, lastSum + nums[i])
            lastSum = tmp
        print maxSum
        return maxSum
    
sl = Solution()
sl.rob([4,3,2,5,7,4,3,1])