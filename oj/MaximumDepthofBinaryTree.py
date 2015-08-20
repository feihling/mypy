#coding=utf-8
'''
Created on 2015.5.30

@author: FEIHUA
'''
# Definition for a binary tree node.
from macpath import curdir
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        print(root.val)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(3)
rtree = TreeNode(6)
troot.left = ltree
troot.right = rtree
rtree.left = TreeNode(2)
rtree.right = TreeNode(8)
print(sl.maxDepth(troot))