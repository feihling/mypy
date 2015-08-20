# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        return self.buildTreeHelper(inorder, postorder, 0, 0, len(postorder))

    def buildTreeHelper(self, inorder, postorder, psIndex, isIndex, subLen):
        if subLen == 0:
            return None
        tRoot = TreeNode(postorder[psIndex + subLen - 1])
        if subLen == 1:
            return tRoot
        rootIndex = inorder.index(postorder[psIndex + subLen - 1])
        curLen = rootIndex - isIndex
        #print(postorder[psIndex:psIndex+curLen], inorder[isIndex:rootIndex])
        #print(postorder[psIndex+curLen:psIndex+subLen-1], inorder[rootIndex+1:isIndex+subLen])
        tRoot.left = self.buildTreeHelper(inorder, postorder, psIndex, isIndex, curLen)
        tRoot.right = self.buildTreeHelper(inorder, postorder, psIndex + curLen, rootIndex + 1, subLen - curLen - 1)
        return tRoot

sl = Solution()
sl.buildTree([1, 2, 3, 4, 5, 6], [1, 3, 2, 5, 6, 4])