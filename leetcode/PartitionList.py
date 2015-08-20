'''
Created on 2015-7-23

@author: lingfeihua
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        dummy_head = ListNode(0)
        p = head
        cur = dummy_head
        par = dummy_head
        while p is not None:
            if p.val < x:
                if par.next == None:
                    par.next = ListNode(p.val)
                    par = par.next
                    cur = par
                else:
                    tmp = par.next
                    par.next = ListNode(p.val)
                    par = par.next
                    par.next = tmp
            else:
                cur.next = ListNode(p.val)
                cur = cur.next
            p = p.next
        return dummy_head.next

sl = Solution()
#node_list = [1,3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1,1,2,2,2,1,2,1,1,2,3,3,2,2,3,2,3,2,2,2,1,1,3,2,3,3,1,1,1,3]
node_list = [10, 9, 8, 7, 6, 11]
dummp_head = ListNode(0)
cur_node = dummp_head
for each_node in node_list:
    cur_node.next = ListNode(each_node)
    cur_node = cur_node.next
lret = sl.partition(dummp_head.next, 8)
l = lret
while l != None:
    print(l.val)
    l = l.next