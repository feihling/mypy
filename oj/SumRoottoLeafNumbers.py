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
    # @return {integer}
    def sumNumbers(self, root):
        if root is None:
            return 0
        return self.rootLeafNum(root, 0)
    def rootLeafNum(self, root, addVal):
        addVal = addVal * 10 + root.val
        if root.left is None and root.right is None:
            return addVal
        ret = []
        if root.left is not None:
            ret = self.rootLeafNum(root.left, addVal)
        if root.right is not None:
            ret += self.rootLeafNum(root.right, addVal)
        return ret

troot = TreeNode(1)
lchild = TreeNode(4)
rchild = TreeNode(5)
troot.left = lchild
troot.right = rchild
lchild.left = TreeNode(2)
lchild.right = TreeNode(3)
rchild.left = TreeNode(6)
rchild.right = TreeNode(7)
sl = Solution()
print sl.rootLeafNum(troot, 0)
            