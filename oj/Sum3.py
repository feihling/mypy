'''
Created on 2015-7-28

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        n = len(nums)
        ret = []
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    k -= 1
                    j += 1
        print(ret)
        return ret

sl = Solution()
sl.threeSum([-1, -1, 2, 2, -1, -4])
sl.threeSum([0, 0, 0])
            