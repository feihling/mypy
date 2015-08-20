# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}

    def levelOrder(self, root):
        if root == None:
            return []
        list_tmp = []
        list_tmp.append(root)
        ret = [[]]
        ret[0].append(root.val)
        rightmost = root
        curdepth = 1
        i = 0
        while i < len(list_tmp):
            if list_tmp[i].left != None:
                if len(ret) == curdepth:
                    ret.append([])
                list_tmp.append(list_tmp[i].left)
                ret[curdepth].append(list_tmp[i].left.val)
            if list_tmp[i].right != None:
                list_tmp.append(list_tmp[i].right)
                ret[curdepth].append(list_tmp[i].right.val)
            if list_tmp[i] == rightmost:
                curdepth += 1
                rightmost = list_tmp[-1]
            i += 1
        return ret
