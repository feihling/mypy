import sys
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        sideNode = None
        if root.left is not None:
            if root.right is not None:
                root.left.next = root.right
                sideNode = root.right
            else:
                sideNode = root.left
        else:
            if root.right is not None:
                sideNode = root.right
        if sideNode is not None:
            tmp = root.next
            while tmp is not None:
                if tmp.left is not None:
                    sideNode.next = tmp.left
                    break
                elif tmp.right is not None:
                    sideNode.next = tmp.right
                    break
                tmp = tmp.next
        if root.right is not None:
            self.connect(root.right)
        
        if root.left is not None:
            self.connect(root.left)

valList = [2,1,3,0,7,9,1,2,'#',1,0,'#','#',8,8,'#','#','#','#',7]
nodeList = [TreeLinkNode(valList[0])]
tmp = nodeList[0]
i = 1
j = 1
while i < len(valList):
    if valList[i] != '#':
        tmp.left = TreeLinkNode(valList[i])
        nodeList.append(tmp.left)
    else:
        nodeList.append(None)
    if i + 1 < len(valList):
        if valList[i + 1] != '#':
            tmp.right = TreeLinkNode(valList[i + 1])
            nodeList.append(tmp.right)
        else:
            nodeList.append(None)
    tmp = nodeList[j]
    i += 2
    j += 1
sl = Solution()
sl.connect(nodeList[0])
i = 0
j = 0
while j < len(nodeList):
    while nodeList[j] is None:
        j += 1
    sys.stdout.write(str(nodeList[j].val))
    sys.stdout.write(' ')
    tmp = nodeList[j].next
    while tmp is not None:
        sys.stdout.write(str(tmp.val))
        sys.stdout.write(' ')
        tmp = tmp.next
    print('#\n')
    i += 1
    j = (1 << i) - 1