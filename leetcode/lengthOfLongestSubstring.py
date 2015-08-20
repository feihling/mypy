class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        i = 0
        res = 0
        dict_tmp = {}
        for j in range(len(s)):
            if s[j] not in dict_tmp or dict_tmp[s[j]] < i:
                dict_tmp[s[j]] = j
            else:
                if (j - i) > res:
                    res = j - i
                i = dict_tmp[s[j]] + 1
                dict_tmp[s[j]] = j
        if (j - i) > res:
            res = j - i
        return res

sl = Solution()
print(sl.lengthOfLongestSubstring('abcdbcef'))
