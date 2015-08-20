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
        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect(root.left)
            self.connect(root.right)

sl = Solution()
troot = TreeLinkNode(4)
ltree = TreeLinkNode(5)
rtree = TreeLinkNode(3)
troot.left = ltree
troot.right = rtree
ltree.left = TreeLinkNode(8)
ltree.right = TreeLinkNode(2)
rtree.left = TreeLinkNode(1)
rtree.right = TreeLinkNode(7)
sl.connect(troot)
tmp = troot
print(troot.left.left.next.val)