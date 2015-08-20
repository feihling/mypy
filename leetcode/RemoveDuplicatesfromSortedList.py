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
    # @return {ListNode}
    def deleteDuplicates(self, head):
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre_node = dummy_head
        cur_node = head
        while cur_node.next is not None:
            if cur_node.next.val == cur_node.val:
                pre_node.next = cur_node.next
                cur_node.next = None
                cur_node = pre_node.next
            else:
                pre_node = cur_node
                cur_node = cur_node.next
        return dummy_head.next