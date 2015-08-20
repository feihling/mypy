#coding=utf-8
'''
Created on 2015.5.28

@author: FEIHUA
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        dummyhead = ListNode(0)
        curnode = dummyhead
        tmp1 = head
        while tmp1 != None:
            tmp2 = tmp1.next
            if tmp2 != None:
                tmp = tmp2.next
                curnode.next = tmp2
                curnode = curnode.next
                curnode.next = tmp1
                curnode = curnode.next
                tmp1 = tmp
            else:
                curnode.next = tmp1
                tmp1 = tmp1.next
        return dummyhead.next