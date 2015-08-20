'''
Created on 2015/6/22

@author: FEIHUA
'''
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        tmp = [[]]
        for j in range(n + 1):
            tmp[0].append(j)
        for i in range(1, m + 1):
            tmp.append([])
            for j in range(n + 1):
                if j == 0:
                    tmp[i].append(i)
                else:
                    if word2[j - 1] == word1[i - 1]:
                        tmp[i].append(tmp[i - 1][j - 1])
                    else:
                        tmp[i].append(min(tmp[i - 1][j], tmp[i][j - 1], tmp[i - 1][j - 1]) + 1)
        print(tmp)
        return tmp[m][n]
sl = Solution()
sl.minDistance('word1', 'word2')