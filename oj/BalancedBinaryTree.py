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
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self.maxDepth(root) != -1

    def maxDepth(self, root):
        if root == None:
            return 0
        ldepth = self.maxDepth(root.left)
        if ldepth == -1:
            return -1
        rdepth = self.maxDepth(root.right)
        if rdepth == -1:
            return -1
        if abs(ldepth - rdepth) <= 1:
            return max(ldepth, rdepth) + 1
        else:
            return -1
    
sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(3)
rtree = TreeNode(6)
troot.left = ltree
troot.right = rtree
rtree.left = TreeNode(2)
rtree.right = TreeNode(8)
print(sl.isBalanced(troot))