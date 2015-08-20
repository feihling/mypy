# coding=utf-8
'''
Created on 2015年6月1日

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
    # @return {integer[]}

    def rightSideView(self, root):
        if root == None:
            return []
        list_tmp = [root]
        rightmost = root
        ret = [root.val]
        i = 0
        while i < len(list_tmp):
            if list_tmp[i].left != None:
                list_tmp.append(list_tmp[i].left)
            if list_tmp[i].right != None:
                list_tmp.append(list_tmp[i].right)
            if list_tmp[i] == rightmost:
                if i != len(list_tmp) - 1:
                    rightmost = list_tmp[-1]
                    ret.append(rightmost.val)
            i += 1
        return ret
sl = Solution()
troot = TreeNode(4)
ltree = TreeNode(5)
rtree = TreeNode(3)
troot.left = ltree
troot.right = rtree
ltree.left = TreeNode(8)
ltree.right = TreeNode(2)
# rtree.left = TreeNode(2)
# rtree.right = TreeNode(7)
print(sl.rightSideView(troot))