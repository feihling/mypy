#coding=utf-8
'''
Created on 2015-5-19

@author: FEIHUA
'''
class Solution:
    # @param {string} digits
    # @return {string[]}
    phone_list = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits):
        ret_list = []
        self.bt(ret_list, 0, digits)
        return ret_list
    
    def bt(self, ret_list, nlen, num_list):
        if num_list == None or num_list == '':
            return
        
        strval = self.phone_list[int(num_list[0])]
        if nlen == 0:
            for i in range(len(strval)):
                ret_list.append(strval[i])
            self.bt(ret_list, len(strval), num_list[1:])
        else:
            for i in range(len(strval)):
                if i == 0:
                    for j in range(nlen):
                        ret_list[j] += strval[i]
                else:
                    for j in range(nlen):
                        ret_list.append(ret_list[j][:-1] + strval[i])
            if len(strval) == 0:
                self.bt(ret_list, nlen, num_list[1:])
            else:
                self.bt(ret_list, nlen * len(strval), num_list[1:])

sl = Solution()
print(sl.letterCombinations('0123456789'))