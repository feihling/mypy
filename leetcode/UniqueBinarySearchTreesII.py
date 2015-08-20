'''
Created on 2015/6/14

@author: FEIHUA
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        tmp = []
        for i in range(max(3, n + 1)):
            tmp.append([])
        tmp[0].append(None)
        tmp[1].append(TreeNode(1))
        tmp[2].append(TreeNode(1))
        tmp[2][0].right = TreeNode(2)
        tmp[2].append(TreeNode(2))
        tmp[2][1].left = TreeNode(1)
        for i in range(3, n + 1):
            for j in range(1, i + 1):
                for k in range(len(tmp[j - 1])):
                    for l in range(len(tmp[i - j])):
                        tmp[i].append(TreeNode(j))
                        tmp[i][-1].left = tmp[j - 1][k]
                        tmp[i][-1].right = self.add(tmp[i - j][l], j)                
        print(len(tmp[n]))
        return tmp[n]

    def add(self, root, val):
        if root is None:
            return None
        tRoot = TreeNode(root.val + val)
        if root.left is not None:
            tRoot.left = self.add(root.left, val)
        if root.right is not None:
            tRoot.right = self.add(root.right, val)
        return tRoot
sl = Solution()
sl.generateTrees(4)