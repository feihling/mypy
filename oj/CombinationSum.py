#coding=utf-8
'''
Created on 2015.5.16

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        cand_tmp = sorted(candidates)
        len_c = len(candidates)
        list_ret = []
        list_tmp = []
        self.bt(cand_tmp, list_ret, list_tmp, 0, 0, len_c, target)
        return list_ret

    def bt(self, cand_tmp, list_ret, list_tmp, num, num_sum, count, target):
        print('num(%s):%s:num_sum(%s)' % (num, list_tmp, num_sum))
        if num_sum == target:
            list_ret.append(list_tmp[:])
            return
        
        if num_sum < target and cand_tmp[num] <= target - num_sum:
            num_sum += cand_tmp[num]
            print('num_sum(%s)' % num_sum)
            list_tmp.append(cand_tmp[num])
            print('append ', list_tmp)
            self.bt(cand_tmp, list_ret, list_tmp, num, num_sum, count, target)
            #only one element
            #if len(list_tmp) < 2:
            #    return
            #pop twice
            num_sum -= cand_tmp[num]
            print('num_sum(%s)' % num_sum)
            list_tmp.pop()
            print('pop ', list_tmp)

        if num < count - 1 and cand_tmp[num + 1] <= target - num_sum:
            self.bt(cand_tmp, list_ret, list_tmp, num + 1, num_sum, count, target)
            
sl = Solution()
print(sl.combinationSum([1, 2], 4))
print(sl.combinationSum([2,3,6,7], 7))