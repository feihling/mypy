#coding=utf-8
'''
Created on 2015.5.19

@author: FEIHUA
'''
class Solution:
    # @param {integer} n
    # @return {integer[]}
#     def grayCode(self, n):
#         if n == 0:
#             return [0]
#         ret_list = self.grayCode(n - 1)
#         ret_tmp = ret_list[:]
#         i = len(ret_tmp) - 1
#         while i >= 0:
#             ret_list.append(ret_tmp[i] + 2 ** (n - 1))
#             i -= 1
#         return ret_list
    def grayCode(self, n):
        ret_list = []
        for i in range(2**n):
            g = (i >> 1) ^ i
            ret_list.append(g)
        return ret_list

sl = Solution()
print(sl.grayCode(3))