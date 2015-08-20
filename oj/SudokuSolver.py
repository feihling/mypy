#coding=utf-8
'''
Created on 2015.5.17

@author: FEIHUA
'''
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    bsolved = False
    def solveSudoku(self, board):
        self.bt(0,0,board)
        return

    def is_value_valid(self, nrow, ncol, nvalue, list_value):
        #print('is valid nrow(%s):ncol(%s):nvalue(%s):list_value[%s]:%s' % (nrow, ncol, nvalue, nrow, list_value[nrow]))
        for i in range(9):
            if list_value[i][ncol] == str(nvalue):
                return False
            if list_value[nrow][i] == str(nvalue):
                return False
        k = nrow // 3
        l = ncol // 3
        for i in range(3):
            for j in range(3):
                if list_value[k * 3 + i][l * 3 + j] == str(nvalue):
                    return False
            
        return True
    
    def bt(self, nrow, ncol, list_value):
#         while nrow < 9 and list_value[nrow][ncol] != '.':
#             if ncol < 8:
#                 ncol += 1
#             else:
#                 nrow += 1
#                 ncol = 0
        if self.bsolved:
            return
        
        if nrow >= 9:
            self.bsolved = True
            return
        
        if list_value[nrow][ncol] == '.':
            for i in range(1, 10):
                if self.is_value_valid(nrow, ncol, i, list_value):
                    list_value[nrow][ncol] = str(i)
                    print('nrow(%s):ncol(%s):nvalue(%s):list_value[%s]:%s' % (nrow, ncol, i, nrow, list_value[nrow]))
                    if ncol < 8:
                        self.bt(nrow, ncol + 1, list_value)
                    else:
                        self.bt(nrow + 1, 0, list_value)
                    if not self.bsolved:
                        list_value[nrow][ncol] = '.'
        else:
            if ncol < 8:
                self.bt(nrow, ncol + 1, list_value)
            else:
                self.bt(nrow + 1, 0, list_value)

sl = Solution()
value_list = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
              ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
              ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
              ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
              ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
              ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
              ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
              ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
              ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
sl.solveSudoku(value_list)
for i in range(9):
    print(value_list[i])
