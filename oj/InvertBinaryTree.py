import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)

valList = [2,1,3,0,7,9,1,2,'#',1,0,'#','#',8,8,'#','#','#','#',7]
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
sl = Solution()
sl.invertTree(nodeList[0])
tmp = nodeList[0]
sideNode = nodeList[0]
list_tmp = [tmp]
i = 0
while i < len(list_tmp):
    sys.stdout.write(str(list_tmp[i].val))
    sys.stdout.write(' ')
    if list_tmp[i].left is not None:
        list_tmp.append(list_tmp[i].left)
    if list_tmp[i].right is not None:
        list_tmp.append(list_tmp[i].right)
    if list_tmp[i] == sideNode:
        sys.stdout.write('\n')
        sideNode = list_tmp[-1]
    i += 1
