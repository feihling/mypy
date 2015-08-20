#coding=utf-8
'''
Created on 2015.5.17

@author: FEIHUA
'''
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        list_ret = []
        list_tmp = []
        for i in range(n):
            list_tmp.append(['.'] * n)
        self.bt(list_ret, list_tmp, 0, n)
        return list_ret
    
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
    
    def bt(self, list_ret, list_tmp, nrow, ncount):
        print('nrow(%s)' % nrow)
        if nrow == ncount:
            print('append ', list_tmp)
            tmp = []
            for i in range(ncount):
                tmp.append(''.join(list_tmp[i]))
            list_ret.append(tmp)
            return
        for ncol in range(ncount):
            if self.is_valid_pos(nrow, ncol, list_tmp, ncount):
                list_tmp[nrow][ncol] = 'Q'
                print('nrow(%s):ncol(%s)' % (nrow, ncol))
                print('list_tmp_append ', list_tmp)
                self.bt(list_ret, list_tmp, nrow + 1, ncount)
                list_tmp[nrow][ncol] = '.'
                print('list_tmp_pop ', list_tmp)

sl = Solution()       
print(sl.solveNQueens(8))