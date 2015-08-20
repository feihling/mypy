# coding=utf-8
'''
Created on 2015.6.1

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
    # @return {integer[][]}

    def zigzagLevelOrder(self, root):
        if root == None:
            return [[]]
        breverse = False
        list_tmp = [root]
        ret = [[root.val]]
        edgenode = root
        i = 0
        nstart = 0
        while i < len(list_tmp):
            if list_tmp[i].left != None:
                list_tmp.append(list_tmp[i].left)
            if list_tmp[i].right != None:
                list_tmp.append(list_tmp[i].right)
            if list_tmp[i] == edgenode:
                ret_tmp = []
                if breverse:
                    j = i
                    while j > nstart:
                        ret_tmp.append(list_tmp[j].val)
                        j -= 1
                else:
                    j = nstart + 1
                    while j <= i:
                        ret_tmp.append(list_tmp[j].val)
                        j += 1
                if ret_tmp != []:
                    ret.append(ret_tmp)
                edgenode = list_tmp[-1]
                breverse = not breverse
                nstart = i
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
rtree.left = TreeNode(6)
rtree.right = TreeNode(7)
print(sl.zigzagLevelOrder(troot))