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
    def preorderTraversal1(self, root):
        ret = []
        if root is None:
            return ret
        ret.append(root.val)
        if root.left is not None:
            ret += self.preorderTraversal(root.left)
        if root.right is not None:
            ret += self.preorderTraversal(root.right)
        
        return ret

    def preorderTraversal(self, root):
        if root is None:
            return []
        ret = []
        list_tmp = []
        tmp = root
        while True:        
            ret.append(tmp.val)
            if tmp.left is not None:
                if tmp.right is not None:
                    list_tmp.append(tmp.right)
                tmp = tmp.left
            else:
                if tmp.right is not None:
                    tmp = tmp.right
                else:
                    if len(list_tmp) == 0:
                        break
                    tmp = list_tmp[-1]
                    list_tmp.pop()
        
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
print sl.preorderTraversal(troot)