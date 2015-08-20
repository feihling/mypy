'''
Created on 2015-6-24

@author: lingfeihua
'''
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        i = 0
        j = 0
        while True:
            if s3[i]