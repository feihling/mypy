'''
Created on 2015-7-23

@author: FEIHUA
'''
# Definition for singly-linked list.
from django.core.cache.backends.locmem import dummy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None:
            return None
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre_node = dummy_head 
        cur_node = head
        cur_val = None
        while cur_node is not None:
            if cur_node.next is not None:
                if cur_node.val == cur_node.next.val:
                    cur_val = cur_node.val
            if cur_val == cur_node.val:
                pre_node.next = cur_node.next
                cur_node.next = None
            else:
                pre_node = cur_node
                cur_node = cur_node.next
        return dummy_head.next
                cur_node = pre_node.next