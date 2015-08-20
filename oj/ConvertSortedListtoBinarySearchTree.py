#coding=utf-8
'''
Created on 2015.5.31

@author: FEIHUA
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    mhead = None
    def sortedListToBST(self, head):
        tmp = head
        nlen = 0
        while tmp != None:
            tmp = tmp.next
            nlen += 1
        self.mhead = head
        return self.sortedListToBSTAst(0, nlen - 1)
        
    def sortedListToBSTAst(self, nstart, nend):
        if nstart > nend:
            return None
        nmid = (nstart + nend) // 2
        #print('nstart(%s) nend(%s) mid(%s)' % (nstart, nend, nmid))
        lchild = self.sortedListToBSTAst(nstart, nmid - 1)
        #print('nstart(%s) nend(%s) value(%s)' % (nstart, nend, self.mhead.val))
        tparent = TreeNode(self.mhead.val)
        self.mhead = self.mhead.next
        tparent.left = lchild
        rchild = self.sortedListToBSTAst(nmid + 1, nend)
        tparent.right = rchild
        return tparent
n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n0.next = n1
n1.next = n2
n2.next = n3
sl = Solution()
sl.sortedListToBST(n0)