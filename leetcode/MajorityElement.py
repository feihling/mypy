from itertools import count
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = 0
        j = nums[0]
        for i in range(len(nums)):
            print(count)
            if count == 0:
                j = nums[i]
            if nums[i] == j:
                count += 1
            else:
                count -= 1
        return j

sl = Solution()
print(sl.majorityElement([1,1,2,2,2,3,3,4,4,3,3,3,3,3]))