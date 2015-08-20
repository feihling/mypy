#coding=utf-8
'''
Created on 2015-5-20

@author: FEIHUA
'''
class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows < 1:
            return
        
        if numRows == 1:
            return [[1],]
        ret_tmp = self.generate(numRows - 1)
        #print('ret_tmp ', ret_tmp)
        list_nrow = []
        list_nrow.append(1)
        i = 0
        while i < len(ret_tmp[-1]) - 1:
            list_nrow.append(ret_tmp[-1][i] + ret_tmp[-1][i + 1])
            i += 1
        list_nrow.append(1)
        ret_tmp.append(list_nrow)
        return ret_tmp
    
sl = Solution()
print(sl.generate(5))