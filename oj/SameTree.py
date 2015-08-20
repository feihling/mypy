#coding=utf-8
'''
Created on 2015.5.31

@author: FEIHUA
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p == None:
            return q== None
        if q ==None:
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True

sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(3)
rtree = TreeNode(6)
troot.left = ltree
troot.right = rtree
rtree.left = TreeNode(2)
rtree.right = TreeNode(8)

troot1 = TreeNode(4)
ltree1 = TreeNode(3)
rtree1 = TreeNode(6)
troot1.left = ltree1
troot1.right = rtree1
rtree1.left = TreeNode(2)
rtree1.right = TreeNode(7)

print(sl.isSameTree(troot, troot1))