#coding=utf-8
'''
Created on 2015.5.17

@author: FEIHUA
'''
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        cand_tmp = sorted(candidates)
        len_c = len(candidates)
        list_ret = []
        list_tmp = []
        self.bt(cand_tmp, list_ret, list_tmp, 0, 0, len_c, target)
        return list_ret

    def bt(self, cand_tmp, list_ret, list_tmp, num, num_sum, count, target):
        print('num(%s):%s:num_sum(%s):count(%s)' % (num, list_tmp, num_sum, count))
        if num_sum == target:
            if list_tmp not in list_ret:
                list_ret.append(list_tmp[:])
            return
        
        if num_sum < target and num < count and cand_tmp[num] <= target - num_sum:
            num_sum += cand_tmp[num]
            print('num_sum(%s)' % num_sum)
            list_tmp.append(cand_tmp[num])
            print('append ', list_tmp)
            self.bt(cand_tmp, list_ret, list_tmp, num + 1, num_sum, count, target)
            num_sum -= cand_tmp[num]
            print('num_sum(%s)' % num_sum)
            list_tmp.pop()

        if num < count - 1 and cand_tmp[num + 1] <= target - num_sum:
            self.bt(cand_tmp, list_ret, list_tmp, num + 1, num_sum, count, target)
            
sl = Solution()
print(sl.combinationSum2([10,1,2,7,6,1,5], 8))
print(sl.combinationSum2([1, 1], 2))