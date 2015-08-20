'''
Created on 2015-7-22

@author: FEIHUA
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd1(self, head, n):
        p1 = head
        len_list = 0
        while p1 is not None:
            len_list += 1
            p1 = p1.next
        if n > len_list:
            return head
        node_index = len_list - n
        i = 0
        dummy_head = ListNode(0)
        dummy_head.next = head
        p1 = dummy_head
        while i < node_index:
            p1 = p1.next
            i += 1
        tmp = p1.next
        p1.next = tmp.next
        tmp.next = None
        return dummy_head.next
    
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(0)
        dummy_head.next = head
        fast_node = head
        while n > 0:
            fast_node = fast_node.next
            n -= 1
        pre_slow = dummy_head
        slow_node = head
        while fast_node is not None:
            pre_slow = slow_node
            slow_node = slow_node.next
            fast_node = fast_node.next
        pre_slow.next = slow_node.next
        return dummy_head.next