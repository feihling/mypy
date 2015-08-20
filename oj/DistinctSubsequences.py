'''
Created on 2015-6-19

@author: lingfeihua
'''
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    ret = 0
    def numDistinct1(self, s, t):
        if len(t) == 0:
            return 1
        if len(s) == 0:
            return 0
        m = len(t)
        n = len(s)
        tmp = [[]]
        if t[0] == s[0]:
            tmp[0].append(1)
        else:
            tmp[0].append(0)
        for j in range(1, n):
            if s[j] == t[0] :
                tmp[0].append(tmp[0][j - 1] + 1)
            else:
                tmp[0].append(tmp[0][j - 1])
        for i in range(1, m):
            print(tmp)
            tmp.append([])
            for j in range(n):
                if j >= i:
                    if s[j] == t[i]:
                        tmp[i].append(tmp[i - 1][j - 1] + tmp[i][j - 1])
                    else:
                        tmp[i].append(tmp[i][j - 1])
                else:
                    tmp[i].append(0)
        #print(tmp)
        return tmp[m - 1][n - 1]

    def numDistinct2(self, s, t):
        m = len(t)
        n = len(s)
        if n < m:
            return 0
        if m == 0:
            return 1
        tmp = [[]]
        if t[0] == s[0]:
            tmp[0].append(1)
        else:
            tmp[0].append(0)
        for j in range(1, n):
            if s[j] == t[0] :
                tmp[0].append(tmp[0][j - 1] + 1)
            else:
                tmp[0].append(tmp[0][j - 1])
        for i in range(1, m):
            tmp.append([])
            if s[i] == t[i]:
                tmp[i].append(tmp[i - 1][0])
            else:
                tmp[i].append(0)
            for j in range(1, n - i):
                if s[i + j] == t[i]:
                    tmp[i].append(tmp[i][j - 1] + tmp[i - 1][j])
                else:
                    tmp[i].append(tmp[i][j - 1])
        print(tmp)
        return tmp[m - 1][n - m]

    def numDistinct(self, s, t):
        m = len(t)
        n = len(s)
        if n < m:
            return 0
        tmp1 = 0
        tmp2 = 1
        cur = 0
        for i in range(m):
            for j in range(1, n - i):
                if s[i + j] == t[i]:
                    cur = tmp1 + tmp2
                else:
                    cur = tmp1

sl = Solution()
sl.numDistinct2('rabbbit', 'rabbit')
sl.numDistinct2('abcbc', 'bcb')
sl.numDistinct2('aabb', 'abb')