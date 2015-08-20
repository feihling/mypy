'''
Created on 2015/6/18

@author: FEIHUA
'''
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        m = len(triangle)
        if m == 0:
            return 0
        tmp = [[triangle[0][0]]]
        for i in range(1, m):
            tmp.append([])
            for j in range(i + 1):
                if j == 0:
                    tmp[i].append(tmp[i - 1][j] + triangle[i][j])
                elif j == i:
                    tmp[i].append(tmp[i - 1][j - 1] + triangle[i][j])
                else:
                    tmp[i].append(min(tmp[i - 1][j - 1], tmp[i - 1][j]) + triangle[i][j])
        print(tmp)
        return min(tmp[m - 1])

sl = Solution()
sl.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,3,8,1]
])
    