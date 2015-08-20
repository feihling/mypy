#coding=utf-8
'''
Created on 2015.5.16

@author: FEIHUA
'''
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        list_ret = []
        list_tmp = []
        self.bt(list_ret, list_tmp, 1, k, n)
        return list_ret

    def bt(self, list_ret, list_tmp, num, k, n):
        if k == 0:
            #print('append ', list_tmp)
            list_ret.append(list_tmp[:])
            return
        
        if k > 0:
            list_tmp.append(num)
            #print(list_tmp)
            self.bt(list_ret, list_tmp, num + 1, k - 1, n)
            list_tmp.pop()
            #print('num(%s):k(%s)' % (num, k))
        
        #n+1-m more than numbers need to compare
        if n - num >= k:
            self.bt(list_ret, list_tmp, num + 1, k, n)

sl = Solution()
print(sl.combine(4, 3))