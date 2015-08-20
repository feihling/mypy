# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}

    def levelOrderBottom(self, root):
        if root == None:
            return []
        list_tmp = []
        list_tmp.append(root)
        rightmost = root
        i = 0
        list_index = []
        while i < len(list_tmp):
            if list_tmp[i].left != None:
                list_tmp.append(list_tmp[i].left)
            if list_tmp[i].right != None:
                list_tmp.append(list_tmp[i].right)
            if list_tmp[i] == rightmost:
                rightmost = list_tmp[-1]
                list_index.append(i)
            i += 1
        ret = []
        i = len(list_index) - 1
        while i > 0:
            ret_tmp = []
            j = list_index[i - 1] + 1
            #print('start(%s) end(%s)' % (list_index[i - 1], list_index[i]))
            while j <= list_index[i]:
                ret_tmp.append(list_tmp[j].val)
                j += 1
            ret.append(ret_tmp)
            i -= 1
        ret.append([root.val])
        return ret

troot = TreeNode(1)
troot.left = TreeNode(2)
troot.right = TreeNode(3)
sl = Solution()
print sl.levelOrderBottom(troot)
