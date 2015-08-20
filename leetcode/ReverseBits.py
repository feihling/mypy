'''
Created on 2015-5-28

@author: lingfeihua
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        nlen = 31
        while n > 0:
            ret += (n % 2) * (2 ** nlen)
            n = n >> 1
            nlen -= 1
            #print 'n:%s' % n
        return ret
    
sl = Solution()
print sl.reverseBits(1)