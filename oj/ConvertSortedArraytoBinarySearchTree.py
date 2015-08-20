#coding=utf-8
'''
Created on 2015.5.31

@author: FEIHUA
'''
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if nums == None or nums == []:
            return None
        print(nums)
        nlow = 0
        nhigh = len(nums) - 1
        mid = (nlow + nhigh) // 2
        print('nlow(%s) nhigh(%s) mid(%s)' % (nlow, nhigh, mid))
        headnode = TreeNode(nums[mid])
        headnode.left = self.sortedArrayToBST(nums[:mid])
        headnode.right = self.sortedArrayToBST(nums[mid + 1:])
        return headnode
sl = Solution()
ret = sl.sortedArrayToBST([0,1,2,3,4,5,6])
list_node = []
if ret != None:
    list_node.append(ret)
    sys.stdout.write(str(ret.val))
    sys.stdout.write('\n')
    i = 0
    rightmost = ret
    while list_node[i].left != None or list_node[i].right != None:
        if list_node[i].left != None:
            list_node.append(list_node[i].left)
            sys.stdout.write(str(list_node[i].left.val))
        if list_node[i].right != None:
            list_node.append(list_node[i].right)
            sys.stdout.write(str(list_node[i].right.val))
        if list_node[i] == rightmost:
            sys.stdout.write('\n')
            if list_node[i].right != None:
                rightmost = list_node[i].right
            else:
                rightmost = list_node[i].left
        i += 1