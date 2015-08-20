'''
Created on 2015-6-8

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
    def postorderTraversal1(self, root):
        if root is None:
            return []
        ret = []
        if root.left is not None:
            ret = self.postorderTraversal(root.left)
        if root.right is not None:
            ret += self.postorderTraversal(root.right)
        ret += [root.val]
        return ret

    def postorderTraversal(self, root):
        if root is None:
            return []
        ret = []
        list_tmp = []
        tmp = root
        while True:
            if tmp.left is None and tmp.right is None:
                ret.append(tmp.val)
                if len(list_tmp) == 0:
                    break
                tmp = list_tmp[-1]
                list_tmp.pop()
            else:
                list_tmp.append(TreeNode(tmp.val))
                if tmp.left is not None:
                    if tmp.right is not None:
                        list_tmp.append(tmp.right)
                    tmp = tmp.left
                else:
                    tmp = tmp.right
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
print sl.postorderTraversal(troot)