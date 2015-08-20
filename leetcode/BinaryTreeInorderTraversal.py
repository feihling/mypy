'''
Created on 2015-6-11

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
    # @return {integer[]}
    def inorderTraversal1(self, root):
        if root is None:
            return []
        ret = []
        if root.left is not None:
            ret = self.inorderTraversal(root.left)
        ret += [root.val]
        if root.right is not None:
            ret += self.inorderTraversal(root.right)
        return ret
    def inorderTraversal(self, root):
        if root is None:
            return []
        ret = []
        list_tmp = []
        tmp = root
        while True:
            if tmp.left is None:
                ret.append(tmp.val)
                if tmp.right is not None:
                    tmp = tmp.right
                if len(list_tmp) == 0:
                    break
                tmp = list_tmp[-1]
                list_tmp.pop()
            else:
                if tmp.right is not None:
                    list_tmp.append(tmp.right)
                list_tmp.append(TreeNode(tmp.val))
                tmp = tmp.left
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
print sl.inorderTraversal(troot)