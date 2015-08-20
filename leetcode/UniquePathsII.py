'''
Created on 2015/6/17

@author: FEIHUA
'''
class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        tmp = []
        for i in range(m):
            tmp.append([])
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    tmp[i].append(0)
                else:
                    if i == 0 and j == 0:
                        tmp[i].append(1)
                    elif i == 0:
                        tmp[i].append(tmp[i][j - 1])
                    elif j == 0:
                        tmp[i].append(tmp[i - 1][j])
                    else:
                        tmp[i].append(tmp[i][j - 1] + tmp[i - 1][j])
        print(tmp)
        return tmp[m - 1][n - 1]

sl = Solution()
sl.uniquePathsWithObstacles([[0, 1, 0],
                             [0, 1, 0],
                             [0, 0, 0],
                             [0, 0, 0]])