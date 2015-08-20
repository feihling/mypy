'''
Created on 2015-6-24

@author: lingfeihua
'''
class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        n = len(s)
        if n == 0:
            return 0        
        tmp = []
        list_tmp = []
        for i in range(n):
            if s[i] == '(':
                list_tmp.append(i)
                tmp.append(0)
            else:             
                if len(list_tmp) != 0:
                    bIndex = list_tmp.pop()
                    if bIndex > 0:
                        tmp.append(tmp[bIndex - 1] + (i - bIndex + 1))
                    else:
                        tmp.append(i - bIndex + 1)
                else:
                    tmp.append(0)
        print tmp
        return max(tmp)


sl = Solution()
sl.longestValidParentheses(')()())')
sl.longestValidParentheses(')()())(')
sl.longestValidParentheses(')()())(((())')
sl.longestValidParentheses("()(()")
sl.longestValidParentheses("()(())")
sl.longestValidParentheses("()()()(())")