'''
Created on 2015-5-28

@author: lingfeihua
'''
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len(needle):
                return i
            i += 1
        #len(haystack) == 0
        return - 1

sl = Solution()
print sl.strStr('abcdefg', 'efg')
print sl.strStr('aaaba', 'ba')