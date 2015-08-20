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
    # @return {integer}
    maxsum = None
    def maxPathSum(self, root):
        self.nodemaxPathSum(root)
        return self.maxsum
    
    def nodemaxPathSum(self, tnode):
        if tnode == None:
            return 0
        lsum = self.nodemaxPathSum(tnode.left)
        print('left sum: %s' % lsum)
        rsum = self.nodemaxPathSum(tnode.right)
        print('right sum: %s' % rsum)
        if self.maxsum == None:
            self.maxsum = lsum + rsum + tnode.val
        else:
            self.maxsum = max(lsum + rsum + tnode.val, self.maxsum)
        ret = max(lsum, rsum) + tnode.val
        if ret < 0:
            return 0
        else:
            return ret
    
sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(3)
rtree = TreeNode(6)
troot.left = ltree
troot.right = rtree
rtree.left = TreeNode(2)
rtree.right = TreeNode(8)
print(sl.maxPathSum(troot))