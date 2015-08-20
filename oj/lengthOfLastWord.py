class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        len_s = len(s)
        i = len_s - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        j = i
        while j >= 0:
            if s[j] == ' ':
                return i - j
            j -= 1
        return i + 1

sl = Solution()
print(sl.lengthOfLastWord("Hello World"))
print(sl.lengthOfLastWord(""))
print(sl.lengthOfLastWord("   "))
print(sl.lengthOfLastWord("ab  "))
