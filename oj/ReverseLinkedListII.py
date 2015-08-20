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
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre_mnode = dummy_head
        i = 1
        while i < m:
            pre_mnode = pre_mnode.next
            i += 1
        m_node = pre_mnode.next
        cur_node = m_node
        next_node = cur_node.next
        while i < n:
            tmp = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = tmp
            i += 1
        n_node = cur_node
        after_nmode = n_node.next
        pre_mnode.next = n_node
        m_node.next = after_nmode
        return dummy_head.next
        