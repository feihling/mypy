'''
Created on 2015-7-29

@author: lingfeihua
'''
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            while s[i] not in t:
                i += 1
            
            while s[j] not in t:
                j -= 1