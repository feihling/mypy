'''
Created on 2015/6/17

@author: FEIHUA
'''
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        pats = p.split('*')
        print(pats)
        return

sl = Solution()
sl.isMatch("aa","a")
sl.isMatch("aa","aa")
sl.isMatch("aaa","aa")
sl.isMatch("aa", "a*")
sl.isMatch("aa", ".*")
sl.isMatch("ab", ".*")
sl.isMatch("aab", "c*a*b")
sl.isMatch("aab", "c*a*b*")