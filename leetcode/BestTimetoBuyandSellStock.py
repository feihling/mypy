#coding=utf-8
'''
Created on 2015.5.23

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        maxPrice = prices[len(prices) - 1]
        ret = 0
        i = len(prices) - 2
        while i >= 0:
            maxPrice = max(maxPrice, prices[i])
            ret = max(ret, maxPrice - prices[i])
            i -= 1  
        return ret

sl = Solution()
print(sl.maxProfit([3, 4, 5, 6, 4, 2, 7, 8]))