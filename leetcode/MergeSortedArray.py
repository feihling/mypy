'''
Created on 2015-7-15

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i + k] > nums2[j]:
                nums1.insert(i + k, nums2[j])
                k += 1
                j += 1
            else:
                i += 1
        if j < n:
            while j < n:
                nums1.insert(i + k, nums2[j])
                k += 1
                j += 1

sl = Solution()
l1 = [4, 5, 6]
l2 = [1, 2, 3]
sl.merge(l1, 3, l2, 3)
print(l1)
l1 = [4, 5, 6]
l2 = [7, 8, 9, 10]
sl.merge(l1, 3, l2, 4)
print(l1)
l1 = [4, 5, 9]
l2 = [6, 7, 8, 9, 10]
sl.merge(l1, 3, l2, 5)
print(l1)
l1 = [0]
l2 = [1]
sl.merge(l1, 0, l2, 1)
print(l1)