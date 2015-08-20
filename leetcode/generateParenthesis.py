#coding=utf-8
'''
Created on 2015.5.16

@author: FEIHUA
'''
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        ret = []
        list_match = []
        self.bt(ret, list_match, 0, 0, n)
        return ret
    
    def bt(self, list_ret, list_match, left, right, num):
        if num == 0 and left == right:
            list_ret.append(''.join(list_match))
            return
    
        if num > 0:
            list_match.append('(')
            self.bt(list_ret, list_match, left + 1, right, num - 1)
            list_match.pop()
        
        if left > right:
            list_match.append(')')
            self.bt(list_ret, list_match, left, right + 1, num)
            list_match.pop()

sl = Solution()
print(sl.generateParenthesis(3))