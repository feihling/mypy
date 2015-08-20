'''
Created on 2015-7-10

@author: lingfeihua
'''
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 != 1:
            n = n >> 1
        return n == 1
    
sl = Solution()
print(sl.isPowerOfTwo(1))