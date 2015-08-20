#coding=utf-8
'''
Created on 2015.5.16

@author: FEIHUA
'''

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        #0   6   12
        #1  57  11
        #2 4 8 10
        #3   9    
        num = numRows + (numRows - 2)
        list_ret = []
        for j in range(numRows):
            if j != 0 and j != numRows - 1:
                for i in range(j, len(s), num):
                    list_ret.append(s[i])
                    if i + num - j*2 < len(s):
                        list_ret.append(s[i + num - j*2])
            else:
                for i in range(j, len(s), num):
                    list_ret.append(s[i])
        return ''.join(list_ret)

sl = Solution()
print(sl.convert("PAYPALISHIRING", 3))