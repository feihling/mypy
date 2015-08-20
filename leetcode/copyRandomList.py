'''
Created on 2015-5-19

@author: lingfeihua
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        tmp = head
        while tmp.next:
            ret = RandomListNode(tmp.label)
            ret.random = tmp.random
            ret.