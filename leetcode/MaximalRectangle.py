'''
Created on 2015-6-24

@author: lingfeihua
'''
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        tmp = []
        for i in range(m):
            tmp.append(matrix[m][:])
        for i in range(m):
            for j in range(n):
                