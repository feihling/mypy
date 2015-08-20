'''
Created on 2015-6-19

@author: lingfeihua
'''
class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        m = len(s)
        tmp = []
        for i in range(m + 1):
            tmp.append(1)
        if s[m - 1] == '0':
            tmp[m - 1] = 0
        else:
            tmp[m - 1] = 1
        i = m - 2
        while i >= 0:
            if s[i] == '0':
                tmp[i] = 0
            elif s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                tmp[i] = tmp[i + 1] + tmp[i + 2]               
            else:
                tmp[i] = tmp[i + 1]                
            i -= 1
        print(tmp)
        return tmp[0]

sl = Solution()
sl.numDecodings('101')
sl.numDecodings('1011')
sl.numDecodings('10116')
sl.numDecodings('10110')
sl.numDecodings('27')
sl.numDecodings('17')
            