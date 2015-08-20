'''
Created on 2015-7-28

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
    def rotateRight(self, head, k):
        if head is None:
            return None
        cur = head
        n = 1
        while cur.next is not None:
            cur = cur.next
            n += 1
        tail = cur
        k = k % n
        if k == 0:
            return head
        self.reverseList(head, tail)
        i = 1
        while i < k:
            cur = cur.next
            i += 1
        rknode = cur
        self.reverseList(rknode.next, head)
        self.reverseList(tail, rknode)
        tail.next = head
        print(rknode.val, rknode.next.val)
        return rknode
    
    def reverseList(self, start, end):
        cur = start
        pre = None
        while cur != end:
            pnext = cur.next
            cur.next = pre
            pre = cur
            cur = pnext
        end.next = pre

sl = Solution()
head = ListNode(1)
head.next = ListNode(2)
sl.rotateRight(head, 1)