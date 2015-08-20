class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        riDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        for i in range(len(s)):
            if i < len(s) - 1 and riDict[s[i]] < riDict[s[i + 1]]:
                ret -= riDict[s[i]]
            else:
                ret += riDict[s[i]]
        return ret

sl = Solution()
print(sl.romanToInt('LXV'))
print(sl.romanToInt('MMMCMXCIX'))