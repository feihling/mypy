'''
Created on 2015-6-18

@author: lingfeihua
'''
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        m = len(s)
        tmp = [True]
        for i in range(1, m + 1):
            tmp.append(False)
            for j in range(i):
                if tmp[j] and s[j:i] in wordDict:
                    tmp[i] = True
                    break
        print(tmp)
        return tmp[m];

sl = Solution()
sl.wordBreak("leetcode", ["etc", "le", "code", 'et'])