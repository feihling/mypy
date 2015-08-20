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
    def isSymmetric1(self, root):
        if root == None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, lchild, rchild):
        if lchild == None:
            return rchild == None
        if rchild == None:
            return False
        if lchild.val != rchild.val:
            return False
        if not self.isMirror(lchild.left, rchild.right):
            return False
        if not self.isMirror(lchild.right, rchild.left):
            return False
        return True

    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isMirror(root.left, root.right)

sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(3)
rtree = TreeNode(3)
troot.left = ltree
troot.right = rtree
ltree.left = TreeNode(8)
ltree.right = TreeNode(2)
rtree.left = TreeNode(2)
rtree.right = TreeNode(8)
print(sl.isSymmetric(troot))