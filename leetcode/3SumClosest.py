'''
Created on 2015-7-28

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0
        min_diff = nums[0] + nums[1] + nums[2] - target
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                diff = nums[i] + nums[j] + nums[k] - target
                if abs(diff) < abs(min_diff):
                    min_diff = diff
                if nums[j] + nums[k] > target - nums[i]:
                    k -= 1
                else:
                    j += 1
        print(target + min_diff)
        return target + min_diff

sl = Solution()
sl.threeSumClosest([-1, 2, 1, -4], 1)