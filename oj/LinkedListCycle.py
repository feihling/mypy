'''
Created on 2015-7-23

@author: lingfeihua
'''
# Definition for singly-linked list.
from email._header_value_parser import Header
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        p1 = p2 = head
        while p1 is not None and p2 is not None:
            p1 = p1.next
            if p2.next is not None:
                p2 = p2.next.next
            else:
                break
            if p1 == p2:
                return True
        return False
    
    def detectCycle(self, head):
        p1 = p2 = head
        bCycle = False
        while p1 is not None and p2 is not None:
            p1 = p1.next
            if p2.next is not None:
                p2 = p2.next.next
            else:
                break
            if p1 == p2:
                bCycle = True
                break
        if bCycle:
            p1 = head
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
        else:
            return None