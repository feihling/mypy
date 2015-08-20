#coding=utf-8
'''
Created on 2015-5-19

@author: FEIHUA
'''
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        list_tmp = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                list_tmp.append(s[i])
            else:
                if len(list_tmp) > 0:
                    if s[i] == ')':
                        if list_tmp[-1] == '(':
                            list_tmp.pop()
                            continue
                    elif s[i] == ']':
                        if list_tmp[-1] == '[':
                            list_tmp.pop()
                            continue
                    elif s[i] == '}':
                        if list_tmp[-1] == '{':
                            list_tmp.pop()
                            continue
                return False
        if len(list_tmp) == 0:
            return True
        else:
            return False
sl = Solution()
print(sl.isValid('('))
print(sl.isValid('()[]{'))