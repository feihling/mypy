'''
Created on 2015-5-28

@author: lingfeihua
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        ret = ''
        j = len(s)
        i = j - 1
        while i >= 0:
            if s[i] == ' ':
                j = i
            elif i == 0 or s[i - 1] == ' ':
                if len(ret) != 0:
                    ret += ' '
                ret += s[i : j]
            i -= 1
        return ret

sl = Solution()
print sl.reverseWords('the sky is blue')
print sl.reverseWords('  a    ')