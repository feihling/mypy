#coding=utf-8
'''
Created on 2015.5.31

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber1(self, nums):
        dictmp = {}
        for i in range(len(nums)):
            if nums[i] not in dictmp:
                dictmp[nums[i]] = 1
            else:
                dictmp[nums[i]] += 1
        for key in dictmp:
            if dictmp[key] == 1:
                return key

    def singleNumber(self, nums):
        nnum = 0
        for eachnum in nums:
            nnum ^= eachnum
        return nnum

sl = Solution()
print(sl.singleNumber([2, 3, 4, 5, 4, 3, 2])) 