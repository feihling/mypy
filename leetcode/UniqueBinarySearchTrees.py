class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        tmp = [0] * (n + 1)
        tmp[0] = 1
        tmp[1] = 1
        tmp[2] = 2
        for i in range(3, n + 1):
            for j in range(1, i + 1):
                tmp[i] += tmp[j - 1]* tmp[i - j]
        print(tmp[n])
        return tmp[n]
sl = Solution()
print(sl.numTrees(4))
sl.numTrees(19)
        