'''
Created on 2015-7-22

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            print(water)
            if water > max_area:
                max_area = water
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        print(max_area)
        return max_area

sl = Solution()
sl.maxArea([1, 2, 3, 4, 5, 6, 2, 3])