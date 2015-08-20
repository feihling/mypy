# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        tmp = root
        nodeList = []
        while tmp.left != None:
            tmp = tmp.left
        nodeList.append(tmp)
        return

valList = [4, 3, 6, 1, 2, 5]
nodeList = [TreeNode(valList[0])]
tmp = nodeList[0]
i = 1
j = 1
while i < len(valList):
    if valList[i] != '#':
        tmp.left = TreeNode(valList[i])
        nodeList.append(tmp.left)
    else:
        nodeList.append(None)
    if i + 1 < len(valList):
        if valList[i + 1] != '#':
            tmp.right = TreeNode(valList[i + 1])
            nodeList.append(tmp.right)
        else:
            nodeList.append(None)
    tmp = nodeList[j]
    i += 2
    j += 1