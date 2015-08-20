#coding=utf-8
'''
Created on 2015。5。19

@author: FEIHUA
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    totalcount = 0
    def totalNQueens(self, n):
        list_tmp = []
        for i in range(n):
            list_tmp.append(['.'] * n)
        self.bt(list_tmp, 0, n)
        return self.totalcount
    
    def is_valid_pos(self, nrow, ncol, list_tmp, ncount):
        for i in range(nrow):
            if list_tmp[i][ncol] == 'Q':
                return False
            if nrow + ncol - i >= 0 and nrow + ncol - i < ncount:
                if list_tmp[i][nrow + ncol - i] == 'Q':
                    return False
            if ncol - nrow + i >= 0 and ncol - nrow + i < ncount:
                if list_tmp[i][ncol - nrow + i] == 'Q':
                    return False
        
        return True
    
    def bt(self, list_tmp, nrow, ncount):
        print('nrow(%s)' % nrow)
        if nrow == ncount:
            self.totalcount += 1
            return
        for ncol in range(ncount):
            if self.is_valid_pos(nrow, ncol, list_tmp, ncount):
                list_tmp[nrow][ncol] = 'Q'
                print('nrow(%s):ncol(%s)' % (nrow, ncol))
                print('list_tmp_append ', list_tmp)
                self.bt(list_tmp, nrow + 1, ncount)
                list_tmp[nrow][ncol] = '.'
                print('list_tmp_pop ', list_tmp)

sl = Solution()       
print(sl.totalNQueens(4))