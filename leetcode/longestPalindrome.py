'''
Created on 2015-5-14

@author: lingfeihua
'''
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            len_s = max(len1, len2)
            if len_s > end - start:
                start = i - (len_s - 1)/2
                end = i + len_s/2
        return s[start:end + 1]
    
    def expandAroundCenter(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
    
sl = Solution()
print sl.longestPalindrome('caba')
print sl.longestPalindrome('eabccb')
print sl.longestPalindrome('bccb')
print sl.longestPalindrome('bcb')
print sl.longestPalindrome(' ')