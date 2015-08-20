#coding=utf-8
'''
Created on 2015.5.30

@author: FEIHUA
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
        dummyhead = RandomListNode(0)
        curnode = dummyhead
        dict_tmp = {}
        while tmp != None:
            curnode.next = RandomListNode(tmp.label)
            dict_tmp[tmp] = curnode.next
            tmp = tmp.next
            curnode = curnode.next
        curnode = dummyhead.next
        tmp = head
        while tmp != None:
            if tmp.random != None:
                curnode.random = dict_tmp[tmp.random]
            else:
                curnode.random = None
            curnode = curnode.next
            tmp = tmp.next
        return dummyhead.next
    
n0 = RandomListNode(0)
n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n0.next = n1
n1.next = n2
n2.next = n3
sl = Solution()
ret = sl.copyRandomList(n0)
n0.next = n2
n2.next = n3
n3.next = n1
while ret != None:
    print(ret.label)
    ret = ret.next