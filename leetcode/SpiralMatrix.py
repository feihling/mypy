class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        i = 0
        while i <= (m // 2):
            print(i)
            #row i
            if i < m - i:
                j = i
                while j < n - i:
                    ret.append(matrix[i][j])
                    j += 1
            #column n - i - 1
            if n - i > i:
                k = i + 1
                while k < m - i - 1:
                    ret.append(matrix[k][n - i - 1])
                    k += 1
            #row m - i - 1
            if i < m - i - 1:
                j = n - i - 1
                while j >= i:
                    ret.append(matrix[m - i - 1][j])
                    j -= 1
            #column i
            if n - i - 1 > i:
                k = m - i - 2
                while k > i:
                    ret.append(matrix[k][i])
                    k -= 1
            i += 1
        print(ret)
        return ret
    

sl = Solution()
# sl.spiralOrder([[ 1, 2, 3, 4],
#                 [ 5, 6, 7, 8],
#                 [ 9,10,11,12],
#                 [13,14,15,16],
#                 [17,18,19,20],
#                 [21,22,23,24]])
#sl.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
sl.spiralOrder([[1,2,3,4],[5,6,7,8]])
#sl.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#sl.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])