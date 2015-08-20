class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        list_ignore = (' ', ',', ':', '.')
        while i < j:
            while i < len(s) and not s[i].isalpha() and not s[i].isdigit():
                i += 1
            while j >= 0 and not s[j].isalpha() and not s[j].isdigit():
                j -= 1
            if i >= j:
                return True            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

sl = Solution()
print(sl.isPalindrome("A man, a plan, a canal: Panama"))
print(sl.isPalindrome("race a car"))
print(sl.isPalindrome(""))
print(sl.isPalindrome(" "))
print(sl.isPalindrome("  "))
print(sl.isPalindrome("a "))
print(sl.isPalindrome("a a"))
print(sl.isPalindrome("a b"))
print(sl.isPalindrome("1 a"))
