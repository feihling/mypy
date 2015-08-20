'''
Created on 2015-5-28

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        i = len(digits) - 1
        ret = digits[:]
        toadd = 1
        while i >= 0:
            if ret[i] > 9:
                toadd = 0
                ret[i] = ret[i] + 1
                break
            else:
                ret[i] = 0
            i -= 1
        if toadd == 1:
            ret.insert(0, 1)
        return ret

sl = Solution()
print(sl.plusOne([1, 2, 3, 4]))
print(sl.plusOne([9]))