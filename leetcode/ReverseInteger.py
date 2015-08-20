'''
Created on 2015-5-28

@author: lingfeihua
'''
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        ret = 0
        while x > 0:
            if 2**31 // 10 < ret:
                return 0
            ret = ret * 10 + x % 10
            x //= 10
        while x < 0:
            if 2**31 // 10 < -ret:
                return 0
            if x % 10 != 0:
                ret = ret * 10 + (x % 10 - 10)
                x = x // 10 + 1
            else:
                ret = ret * 10
                x = x // 10
        return ret

sl = Solution()
print sl.reverse(-200)