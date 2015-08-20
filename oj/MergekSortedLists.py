#coding=utf-8
'''
Created on 2015.5.30

@author: FEIHUA
'''
import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) == 2:
            sys.stdout.write('cur lists: ')
            for e1 in lists:
                sys.stdout.write(str(e1.val))
            sys.stdout.write('\n')
            dummyhead = ListNode(0)
            curnode = dummyhead
            tmp1 = lists[0]
            tmp2 = lists[1]
            while tmp1 and tmp2:
                if tmp1.val < tmp2.val:
                    curnode.next = tmp1
                    tmp1 = tmp1.next
                else:
                    curnode.next = tmp2
                    tmp2 = tmp2.next
                curnode = curnode.next
            if tmp1 != None:
                curnode.next = tmp1
            if tmp2 != None:
                curnode.next = tmp2
            return dummyhead.next
        mid = len(lists) // 2
        return self.mergeKLists([self.mergeKLists(lists[0:mid]), self.mergeKLists(lists[mid:])])

    def mergeKLists1(self, lists):
        dummyhead = ListNode(0)
        curnode = dummyhead
        minlist = []
        for i in range(len(lists)):
            if lists[i] != None:
                k = 0
                l = len(minlist) - 1
                j = 0
                while k <= l:
                    print('low(%s)high(%s)mid(%s)' % (k, l, j))
                    j = (k + l) // 2
                    if lists[i].val < minlist[j].val:
                        k = j + 1
                    else:
                        l = j - 1
                print('low(%s)high(%s)mid(%s)' % (k, l, j))
                if k > len(minlist) - 1:
                    minlist.append(lists[i])
                else:
                    minlist.insert(k, lists[i])
        for tmp in minlist:
            sys.stdout.write(str(tmp.val))
        sys.stdout.write('\n')
        while len(minlist) > 0:
            curnode.next =  minlist[-1]
            curnode = curnode.next
            tmp =  minlist[-1].next
            minlist.pop()
            if tmp != None:
                k = 0
                l = len(minlist) - 1
                j = 0
                while k <= l:
                    j = (k + l) // 2
                    if tmp.val < minlist[j].val:
                        k = j + 1
                    else:
                        l = j - 1
                if k > len(minlist) - 1:
                    minlist.append(tmp)
                else:
                    minlist.insert(k, tmp)
        return dummyhead.next
n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n5 = ListNode(5)
sl = Solution()
ret = sl.mergeKLists([n0, n2, n5, n1])
while ret != None:
    sys.stdout.write(str(ret.val))
    ret = ret.next
sys.stdout.write('\n')
n0.next = n2
n2.next = n5
ret = sl.mergeKLists([n0])
while ret != None:
    sys.stdout.write(str(ret.val))
    ret = ret.next