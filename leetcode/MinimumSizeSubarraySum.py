'''
Created on 2015-7-29

@author: lingfeihua
'''
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if nums == []:
            return 0
        n = len(nums)
        i = 0
        j = 1
        sum_tmp = nums[0]
        min_len = n
        while i < n and j < n:
            while sum_tmp < s and j < n:
                sum_tmp += nums[j]
                j += 1
            while sum_tmp >= s:
                if min_len > j - i:
                    min_len = j - i
                # print(nums[i:j], min_len)
                sum_tmp -= nums[i]
                i += 1
        if min_len == n:
            if sum_tmp < s:
                return 0
        return min_len

sl = Solution()
print(sl.minSubArrayLen(7, [2,3,1,2,4,3]))
print(sl.minSubArrayLen(10, [1, 4, 4]))
print(sl.minSubArrayLen(1, []))