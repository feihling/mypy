'''
Created on 2015-6-11

@author: lingfeihua
'''
# Definition for a binary tree node.
from compiler.syntax import check
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes1(self, root):
        if root is None:
            return 0
        tmp = root
        list_tmp=[root]
        nNum = 0
        while tmp is not None:
            list_tmp.append(tmp.left)
            list_tmp.append(tmp.right)
            nNum += 1
            tmp = list_tmp[nNum]
        return nNum
    def countNodes(self, root):
        if root is None:
            return 0
        tmp = root
        nLevel = 0
        while tmp is not None:
            nLevel += 1
            tmp = tmp.left
        minVal = 0
        maxVal = (1 << (nLevel - 1)) - 1
        while minVal <= maxVal:
            midVal = (minVal + maxVal) // 2
            if self.check(root, midVal, nLevel):
                minVal = midVal + 1
            else:
                maxVal = midVal - 1
        print 'minVal(%s), maxVal(%s), midVal(%s)' % (minVal, maxVal, midVal)
        return minVal - 1 + (1 << (nLevel - 1))
    
    def check(self, root, nVal, nLevel):
        i = nLevel - 2
        nMask = 1 << (nLevel - 1)
        tmp = root
        while i >= 0:
            nMask >>= 1
            if (nVal & nMask) == nMask:
                tmp = tmp.right
            else:
                tmp = tmp.left
            i -= 1
        return tmp is not None

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
print sl.countNodes(troot)