'''
Created on 2015-7-10

@author: lingfeihua
'''
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow1(self, x, n):
        ret = 1
        for i in range(n):
            ret *= x
        print(ret)
        return ret

    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = 0 - n
        if n % 2 == 0:
            ret = self.myPow(x, n//2)
            ret *= ret
            print(ret)
            return ret
        else:
            ret = self.myPow(x, (n - 1)//2)
            ret *= ret * x
            print(ret)
            return ret

sl = Solution()
sl.myPow(5, -3)