'''
Created on 2015-7-29

@author: lingfeihua
'''
class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        ret = numerator/(denominator*1.0)
        decimal = ret - int(ret)
        while decimal != 0:
            decimal = decimal * 10
    
sl = Solution()
print(sl.fractionToDecimal(1, 2))
print(sl.fractionToDecimal(2, 1))
print(sl.fractionToDecimal(2, 3))