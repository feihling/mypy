'''
Created on 2015/6/29

@author: FEIHUA
'''
class Solution:
    def mySort1(self, nums):
        for i in range(1, len(nums)):
            insertNum = nums[i]
            j = i - 1
            #locate, insert after j
            while j >= 0 and insertNum < nums[j]:
                j -= 1
            print(j)
            k = i
            while k > j + 1:
                nums[k] = nums[k - 1]
                k -= 1
            nums[j + 1] = insertNum
        print(nums)
    
    def mySort2(self, nums):
        print(nums)
        n = len(nums)
        if n == 1:
            return nums
        return self.mergeArray(self.mySort2(nums[:n//2]), self.mySort2(nums[n//2:]))

    def mergeArray(self, nums1, nums2):
        i = 0
        j = 0
        ret = []
        print('nums1:', nums1)
        print('nums2:', nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1
        if i == len(nums1):
            while j < len(nums2):
                ret.append(nums2[j])
                j += 1
        else:
            while i < len(nums1):
                ret.append(nums1[i])
                i += 1
        print(ret)
        return ret

sl = Solution()
sl.mySort2([1,2,3,4,5,6])
sl.mySort2([6,5,4,3,2,1])