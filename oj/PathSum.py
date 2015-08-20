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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left != None:
            if self.hasPathSum(root.left, sum - root.val):
                return True
        if root.left == None and root.right == None:
            print('val(%s) sum(%s)' % (root.val, sum))
            if root.val == sum:
                return True
        if root.right != None:
            if self.hasPathSum(root.right, sum - root.val):
                return True
        return False
sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(3)
rtree = TreeNode(6)
troot.left = ltree
troot.right = rtree
rtree.left = TreeNode(2)
rtree.right = TreeNode(8)
print(sl.hasPathSum(troot, 4))