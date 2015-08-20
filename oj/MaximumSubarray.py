'''
Created on 2015-6-18

@author: lingfeihua
'''
from time import sleep
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray1(self, nums):
        m = len(nums)
        if m == 0:
            return 0
        tmp1 = [nums[0]]
        tmp2 = [nums[0]]
        for i in range(1, m):
            tmp2.append(max(nums[i], tmp2[i - 1] + nums[i]))
            tmp1.append(max(tmp1[i - 1], tmp2[i]))
        #print tmp1
        #print tmp2
        return tmp1[m - 1]

    def maxSubArray(self, nums):
        m = len(nums)
        if m == 0:
            return 0
        if m == 1:
            return nums[0]
        if m == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        lSum = self.maxSubArray(nums[: m//2])
        print(nums[:m//2], lSum)
        rSum = self.maxSubArray(nums[m//2:])
        print(nums[m//2:], rSum)
        i = m // 2
        cl = nums[i]
        cr = nums[i + 1]
        clSum = nums[i]
        crSum = nums[i + 1]
        print(clSum, crSum)
        i -= 1
        while i >= 0:
            cl += nums[i]
            if cl > clSum:
                clSum = cl
            i -= 1
        i = m // 2 + 2
        while i < m:
            cr += nums[i]
            if cr > crSum:
                crSum = cr
            i += 1
        print(clSum, crSum)
        return max(lSum, rSum, max(clSum, clSum + crSum))
        
sl = Solution()
#print(sl.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sl.maxSubArray([1,2,-1]))