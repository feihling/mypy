'''
Created on 2015-6-12

@author: lingfeihua
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
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        ret = []
        if root.left is not None:
            lRet = self.pathSum(root.left, sum - root.val)
            for eachItem in lRet:
                eachItem.insert(0, root.val)
            ret = lRet
        if root.right is not None:
            rRet = self.pathSum(root.right, sum - root.val)
            for eachItem in rRet:
                eachItem.insert(0, root.val)
            ret += rRet
        return ret

troot = TreeNode(1)
lchild = TreeNode(6)
rchild = TreeNode(7)
troot.left = lchild
troot.right = rchild
lchild.left = TreeNode(4)
lchild.right = TreeNode(5)
rchild.left = TreeNode(2)
rchild.right = TreeNode(3)
sl = Solution()
print sl.pathSum(troot, 11)
