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
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if root is None:
            return
        rChild = root.right
        if root.left is not None:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            if rChild is not None:
                self.flatten(rChild)        
                while root.right is not None:
                    root = root.right
                root.right = rChild
        else:
            if rChild is not None:
                self.flatten(rChild)
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
sl.flatten(troot)
while troot is not None:
    print troot.val
    troot = troot.right
    