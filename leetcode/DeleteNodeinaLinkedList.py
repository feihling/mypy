'''
Created on 2015-7-22

@author: FEIHUA
'''
# Definition for singly-linked list.
from django.db.migrations.graph import Node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node is None or node.next is None:
            return
        pre_node = node
        cur_node = pre_node.next
        while cur_node.next is not None:
            pre_node.val = cur_node.val
            pre_node = cur_node
            cur_node = cur_node.next
        pre_node.next = None