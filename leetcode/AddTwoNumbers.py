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
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummyhead = ListNode(0)
        curnode = dummyhead
        toaddnext = 0
        while l1 != None or l2 != None:
            curnode.next = ListNode(0)
            curnode = curnode.next
            if l1 == None:
                tmp = l2.val + toaddnext
            elif l2 == None:
                tmp = l1.val + toaddnext
            else:
                tmp = l1.val + l2.val + toaddnext
            if tmp > 9:
                curnode.val = tmp - 10
                toaddnext = 1
            else:
                curnode.val = tmp
                toaddnext = 0
            l1 = l1.next
            l2 = l2.next
        if toaddnext == 1:
            curnode.next = ListNode(1)
            curnode = curnode.next

        curnode.next = None
        return dummyhead.next