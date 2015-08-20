'''
Created on 2015-7-15

@author: lingfeihua
'''
import random
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList1(self, head):
        dummy_head = ListNode(0)
        cur = dummy_head
        cur.next = head
        # cur is the minimum value
        while cur.next != None:
            min_node = cur.next
            pre = cur.next
            tr = cur.next
            while tr.next != None:
                if tr.next.val < min_node.val:
                    min_node = tr.next
                    pre = tr
                tr = tr.next
            if cur.next != min_node:
                pre.next = min_node.next
                min_node.next = cur.next
                cur.next = min_node
            cur = cur.next
        return dummy_head.next
    
    def sortList(self, head):
        tmp = head
        n = 0
        while tmp is not None:
            n += 1
            tmp = tmp.next
        self.sortListHelper(head, None, n)
        return head
    
    def sortListHelper(self, head, tail, list_len):
        if head is None or head == tail or head.next == tail:
            return

        ri = random.randrange(0, list_len)
        i = 0
        rp = head
        while i < ri:
            rp = rp.next
            i += 1
        tmp = rp.val
        rp.val = head.val
        head.val = tmp
        
        p1 = head
        p2 = head.next
        i = 0
        while p2 != tail:
            if p2.val < head.val:
                tmp = p1.next.val
                p1.next.val = p2.val
                p2.val = tmp
                p1 = p1.next
                i += 1
            p2 = p2.next
        tmp = p1.val
        p1.val = head.val
        head.val = tmp
        self.sortListHelper(head, p1, i)
        self.sortListHelper(p1.next, tail, list_len - i - 1)
            

sl = Solution()
#node_list = [1,3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1,1,2,2,2,1,2,1,1,2,3,3,2,2,3,2,3,2,2,2,1,1,3,2,3,3,1,1,1,3]
node_list = [10, 9, 8, 7, 6, 11]
dummp_head = ListNode(0)
cur_node = dummp_head
for each_node in node_list:
    cur_node.next = ListNode(each_node)
    cur_node = cur_node.next
lret = sl.sortList(dummp_head.next)
l = lret
while l != None:
    print(l.val)
    l = l.next