'''
Created on 2015/6/14

@author: FEIHUA
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        tmp = [0] * n
        tmp[0] = 1
        tmp[1] = 2
        for i in range(2, n):
            tmp[i] = tmp[i - 1] + tmp[i - 2]
        print(tmp)
        return tmp[n - 1]

sl = Solution()
sl.climbStairs(3)