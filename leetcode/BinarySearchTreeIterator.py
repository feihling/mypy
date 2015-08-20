'''
Created on 2015-6-11

@author: lingfeihua
'''
# Definition for a  binary tree node
from time import sleep
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.headNode = root
        self.val_list = []
        if root is not None:
            list_tmp = []
            tmp = root
            while True:
                if tmp.right is None:
                    self.val_list.append(tmp.val)
                    if tmp.left is not None:
                        tmp = tmp.left
                    else:
                        if len(list_tmp) == 0:
                            break
                        tmp = list_tmp[-1]
                        list_tmp.pop()
                else:
                    if tmp.left is not None:
                        list_tmp.append(tmp.left)
                    list_tmp.append(TreeNode(tmp.val))
                    tmp = tmp.right      

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.val_list) != 0

    # @return an integer, the next smallest number
    def next(self):        
        return self.val_list.pop()
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())