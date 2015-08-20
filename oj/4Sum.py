'''
Created on 2015-7-22

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum2(self, nums, target):
        nums.sort()
        n = len(nums)
        ret_list = []
        for i in range(n - 3):
            if nums[i] > target/4.0:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                target2 = target - nums[i]
                if nums[j] > target2/3.0:
                    break
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                target3 = target2 - nums[j]
                while k < l:
                    if nums[k] > target3/2.0:
                        break
                    if nums[k] + nums[l] > target3:
                        l -= 1
                    elif nums[k] + nums[l] < target3:
                        k += 1
                    else:
                        ret_list.append([nums[i], nums[j], nums[k], nums[l]])
                        while l > j and nums[l] == nums[l - 1]:
                            l -= 1
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        l -= 1
                        k += 1
        print(ret_list)
        return ret_list
    
    def fourSum1(self, nums, target):
        nums.sort()
        n = len(nums)
        dict_two_sum = {}
        ret = []
        for i in range(n):
            # get rid of repeated sums
            if i > 1 and nums[i] == nums[i - 2]:
                continue
            for j in range(i + 1, n):
                # get rid of repeated pair sums
                if j > i + 2 and nums[j] == nums[j - 2]:
                    continue
                
                # for each pair sum, check if the pair sum that is needed to get the target has been visited
                if target - (nums[i] + nums[j]) in dict_two_sum:
                    # if so, get all the pairs that contribute to this visited pair sum
                    dict_two_sum[target - (nums[i] + nums[j])]

    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if nums[i] > target/4.0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target2 = target - nums[i]
            for j in range(i+1, len(nums)-2):
                if nums[j] > target2/3.0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                target3 = target2 - nums[j]
                # we should use continue not break
                # because target3 changes as j changes
                if nums[k] > target3/2.0:
                    continue
                if nums[l] < target3/2.0:
                    continue
                while k < l:
                    sum_value = nums[k] + nums[l]
                    if sum_value == target3:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        kk = nums[k]
                        k += 1
                        while k<l and nums[k] == kk:
                            k += 1

                        ll = nums[l]
                        l -= 1
                        while k<l and nums[l] == ll:
                            l -= 1
                    elif sum_value < target3:
                        k += 1
                    else:
                        l -= 1
        return result
sl = Solution()
sl.fourSum([1, 0, -1, 0, -2, 2], 0)
sl.fourSum([1, 0, -1, 0, 0, -1, -2, -2, 2, 2], 0)
sl.fourSum([0, 0, 0, 0], 0)