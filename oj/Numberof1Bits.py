'''
Created on 2015-6-12

@author: lingfeihua
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        nMask = 1 << 31
        nBits = 0
        while nMask > 0:
            if n & nMask == nMask:
                nBits += 1
            nMask >>= 1
        return nBits

sl = Solution()
print sl.hammingWeight(11)