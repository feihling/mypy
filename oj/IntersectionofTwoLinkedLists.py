'''
Created on 2015-7-23

@author: lingfeihua
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        m = 0
        p = headA
        while p is not None:
            m += 1
            p = p.next
        n = 0
        p = headB
        while p is not None:
            n += 1
            p = p.next
        k = 0
        if m > n:
            lhead = headA
            shead = headB
            k = m - n
        else:
            lhead = headB
            shead = headA
            k = n - m
        fast_node = lhead
        while k > 0:
            fast_node = fast_node.next
            k -= 1
        slow_node = shead
        while fast_node is not None:
            if fast_node == slow_node:
                return fast_node
            fast_node = fast_node.next
            slow_node = slow_node.next
        
        return None  