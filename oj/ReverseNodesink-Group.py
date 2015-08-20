'''
Created on 2015-7-23

@author: FEIHUA
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        dummy_head = ListNode(0)
        dummy_head.next = head
        i = 0
        cur_node = head
        next
        while i < k:
            p = p.next
            i += 1
        