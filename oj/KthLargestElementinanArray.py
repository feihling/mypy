'''
Created on 2015-6-24

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        print(sorted(nums, reverse=True)[k - 1])

sl = Solution()
sl.findKthLargest([1,2,3,4,5,6], 1)