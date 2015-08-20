#coding=utf-8
'''
Created on 2015.5.30

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
    min = None
    def isValidBST(self, root):
        print(root.val)
        if root == None:
            return True
        if root.left != None:
            if self.isValidBST(root.left) == False:
                return False
        if self.min == None:
            self.min = root.val
        else:
            if root.val <= self.min:
                return False
            else:
                self.min = root.val
        if root.right != None:
            if self.isValidBST(root.right) == False:
                return False
        return True

sl = Solution()
# troot = TreeNode(4)
# ltree = TreeNode(3)
# rtree = TreeNode(6)
# troot.left = ltree
# troot.right = rtree
# rtree.left = TreeNode(2)
# rtree.right = TreeNode(8)
# print(sl.isValidBST(troot))
troot = TreeNode(0)
ltree = TreeNode(-1)
troot.left = ltree
print(sl.isValidBST(troot))