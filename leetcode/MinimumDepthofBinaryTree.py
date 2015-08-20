#coding=utf-8
'''
Created on 2015.5.31

@author: FEIHUA
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth1(self, root):
        if root == None:
            return 0
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth(self, root):
        if root == None:
            return 0
        list_node = []
        list_node.append(root)
        curdepth = 1
        i = 0
        rightmost = root
        while list_node[i].left != None or list_node[i].right != None:
            if list_node[i].left != None:
                list_node.append(list_node[i].left)
            if list_node[i].right != None:
                list_node.append(list_node[i].right)
            if list_node[i] == rightmost:
                curdepth += 1
                if list_node[i].right != None:
                    rightmost = list_node[i].right
                else:
                    rightmost = list_node[i].left
            i += 1
        return curdepth

sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(3)
rtree = TreeNode(6)
troot.left = ltree
troot.right = rtree
rtree.left = TreeNode(2)
rtree.right = TreeNode(8)
print(sl.minDepth(troot))