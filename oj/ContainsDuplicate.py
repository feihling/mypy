'''
Created on 2015-7-29

@author: lingfeihua
'''
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dict_num = {}
        for num in nums:
            if num not in dict_num:
                dict_num[num] = 1
            else:
                return True
        return False
    
    def containsNearbyDuplicate(self, nums, k):
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] not in dict_num:
                dict_num[nums[i]] = i
            else:
                if i - dict_num[nums[i]] <= k:
                    return True
                else:
                    dict_num[nums[i]] = i
        return False
    
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] not in dict_num:
                dict_num[nums[i]] = i
            else:
                return True
        nums.sort()

    def isValidSudoku(self, board):
        for i in range(9):
            if not self.isValidElement(board[i]):
                return False
        
        for i in range(9):
            str_element = ''
            for each_board in board:
                str_element += each_board[i]
            if not self.isValidElement(str_element):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValidElement(board[i][j : j+3] + board[i + 1][j : j + 3] + board[i + 2][j : j+3]):
                    return False
        return True
    
    def isValidElement(self, nums):
        dict_num = {}
        for num in nums:
            if num == '.':
                continue
            if num < '0' or num > '9':
                return False
            if num not in dict_num:
                dict_num[num] = 1
            else:
                return False
        return True

sl = Solution()
ret = sl.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
print(ret)