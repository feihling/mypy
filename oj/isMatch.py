class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        #print 's: %s' % s
        #print 'p: %s' % p
        if p == None:
            return s == None

        if p == '':
            return s == ''
        
        if len(p) == 1:
            if len(s) == 1:
                return s[0] == p[0] or p[0] == '.'
            return False
        
        if p[1] != '*':
            if s == None or s == '':
                return False
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])
            return False
        
#         while s and (s[0] == p[0] or p[0] == '.'):
#             if self.isMatch(s, p[2:]):
#                 return True
#             s = s[1:]
        
        while s :
            if not (s[0] == p[0] or p[0] != '.'):
                return False   
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return False


sl = Solution()
#print(sl.isMatch("aa","a"))
#print(sl.isMatch("aa","aa"))
#print(sl.isMatch("aaa","aa"))
#print(sl.isMatch("aa", "a*"))
#print(sl.isMatch("aa", ".*"))
#print(sl.isMatch("ab", ".*"))
#print(sl.isMatch("aab", "c*a*b"))
#print(sl.isMatch("a", "ab*"))
#print(sl.isMatch("", "a*b*c*d*"))
#print(sl.isMatch("a", ""))
print(sl.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
print(sl.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*b"))
#print(sl.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*bc"))