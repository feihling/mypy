'''
Created on 2015-7-10

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays1(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        tmp = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
        if i < m:
            tmp.extend(nums1[i:])
        if j < n:
            tmp.extend(nums2[j:])
        print(tmp)
        if (m + n) % 2 == 0:
            return (tmp[(m + n)//2] + tmp[(m + n)//2 - 1])/2
        else:
            return tmp[(m + n - 1)//2]

sl = Solution()
print(sl.findMedianSortedArrays([1,2,3,4], [5,6,7,8]))
print(sl.findMedianSortedArrays([1,2,3,4], [5,6,7,8,9]))
print(sl.findMedianSortedArrays([], [2,3]))