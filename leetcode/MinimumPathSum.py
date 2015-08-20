'''
Created on 2015-6-18

@author: lingfeihua
'''
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        tmp = []
        for i in range(m):
            tmp.append([])
            for j in range(n):
                if i == 0 and j == 0:
                    tmp[i].append(grid[i][j])
                elif i == 0:
                    tmp[i].append(tmp[i][j - 1] + grid[i][j])
                elif j == 0:
                    tmp[i].append(tmp[i - 1][j] + grid[i][j])
                else:
                    tmp[i].append(min(tmp[i - 1][j], tmp[i][j - 1]) + grid[i][j])
        print tmp
        return tmp[m - 1][n - 1]

sl = Solution()
sl.minPathSum([[1, 3, 5], [2, 1, 4], [3, 2, 4]])
sl.minPathSum([[1,2],[1,1]])