#coding=utf-8
'''
Created on 2015-5-19

@author: FEIHUA
'''
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        
        base = 1
        while x // base >= 10:
            base = base * 10
        #print('x:%s;base: %s' % (x, base))
        #1000021
        while x > 0:
            leftdigit = x // base 
            rightdigit = x % 10
            #print('left:%s;right: %s' % (leftdigit, rightdigit))
            if leftdigit == rightdigit:
                x = (x - leftdigit * base) // 10
                base = base // 100
                #print('x:%s;base: %s' % (x, base))
            else:
                return False
        
        return True

sl = Solution()
print(sl.isPalindrome(8))
print(sl.isPalindrome(11))
print(sl.isPalindrome(121))
print(sl.isPalindrome(1211))
print(sl.isPalindrome(10))
print(sl.isPalindrome(1000021))