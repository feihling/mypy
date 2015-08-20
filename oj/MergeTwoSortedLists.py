#coding=utf-8
'''
Created on 2015年5月28日

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
    def mergeTwoLists(self, l1, l2):
        dummyhead = ListNode(0)
        curnode = dummyhead
        while l1.next and l2.next:
            if l1.val < l2.val:
                curnode.next = l1
                l1 = l1.next
            else:
                curnode.next = l2
                l2 = l2.next
            curnode = curnode.next
        if l1.next != None:
            curnode.next = l1
        if l2.next != None:
            curnode.next = l2
        return dummyhead.next