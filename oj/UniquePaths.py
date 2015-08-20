'''
Created on 2015-6-15

@author: lingfeihua
'''
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        self.pathSum = 0
        self.uniquePathsHelper(1, 1, m, n)
        print self.pathSum
        return self.pathSum
    def uniquePathsHelper(self, i, j, m, n):
        if i == m and j == n:
            self.pathSum += 1
        print('i: %s, j: %s' % (i, j))
        if i < m:
            i += 1
            self.uniquePathsHelper(i, j, m, n)
            i -= 1
        if j < n:
            j += 1
            self.uniquePathsHelper(i, j, m, n)
            j -= 1

    def uniquePaths1(self, m, n):
        tmp = []
        for i in range(m):
            tmp.append([])
            for j in range(n):
                tmp[i].append(1)
        #print(tmp)
        for i in range(1, m):
            for j in range(1, n):
                tmp[i][j] = tmp[i -1][j] + tmp[i][j - 1]
        print(tmp)
        return(tmp[m - 1][n - 1])
sl = Solution()
#sl.uniquePaths(23, 12)
print(sl.uniquePaths1(3, 3))