# Definition for a binary tree node.Construct Binary Tree from Preorder
# and Inorder Traversal


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}

    def buildTree1(self, preorder, inorder):
        if preorder is None or preorder == []:
            return None
        tRoot = TreeNode(preorder[0])
        if len(preorder) == 1:
            return tRoot
        rootIndex = inorder.index(preorder[0])
        print(preorder[1:rootIndex + 1], inorder[:rootIndex])
        print(preorder[rootIndex + 1:], inorder[rootIndex + 1:])
        tRoot.left = self.buildTree(
            preorder[1:rootIndex + 1], inorder[:rootIndex])
        tRoot.right = self.buildTree(
            preorder[rootIndex + 1:], inorder[rootIndex + 1:])
        return tRoot
    
    def buildTree(self, preorder, inorder):
        if preorder is None or preorder == []:
            return None
        return self.buildTreeHelper(preorder, inorder, 0, 0, len(preorder))
    
    def buildTreeHelper(self, preorder, inorder, psIndex, isIndex, subLen):
        if subLen == 0:
            return None
        tRoot = TreeNode(preorder[psIndex])
        if subLen == 1:
            return tRoot
        rootIndex = inorder.index(preorder[psIndex])
        curLen = rootIndex - isIndex
        #print(preorder[psIndex + 1:psIndex + curLen + 1], inorder[isIndex:rootIndex])
        #print(preorder[psIndex + curLen + 1:psIndex + subLen], inorder[rootIndex + 1:isIndex + subLen])
        tRoot.left = self.buildTreeHelper(preorder, inorder, psIndex + 1, isIndex, curLen)
        tRoot.right = self.buildTreeHelper(preorder, inorder, psIndex + curLen + 1, rootIndex + 1, subLen - curLen - 1)
        return tRoot

sl = Solution()
sl.buildTree([4, 2, 1, 3, 6, 5], [1, 2, 3, 4, 5, 6])
