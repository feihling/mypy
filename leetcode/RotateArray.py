'''
Created on 2015-7-28

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        k = k % n
        self.reverse(nums, 0, n)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k - 1, n)
        print(nums)
    
    def reverse(self, nums, start, end):
        i = start
        j = end - 1
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
            
sl = Solution()
sl.rotate([1, 2, 3, 4, 5, 6, 7], 3)
sl.rotate([1, 2, 3, 4, 5, 6, 7], 2)
            