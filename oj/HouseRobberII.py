'''
Created on 2015-6-18

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        #tmp1 is the maxSum contains nums[0]
        tmp1 = [nums[0], nums[0]]
        #tmp2 is the maxSum not contains nums[0]
        tmp2 = [0, nums[1]]
        tmp = [nums[0], max(nums[0], nums[1])]
        m = len(nums)
        for i in range(2, m):
            tmp1.append(max(tmp1[i - 1], tmp1[i - 2] + nums[i]))
            tmp2.append(max(tmp2[i - 1], tmp2[i - 2] + nums[i]))
            tmp.append(max(tmp[i - 1], tmp[i - 2] + nums[i]))
        print tmp1
        print tmp2
        print tmp
        return max(tmp1[m - 2], tmp2[m - 2], tmp2[m - 3] + nums[m - 1])

sl = Solution()
print(sl.rob([4,3,2,5,7,4,3,6]))
            