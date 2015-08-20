'''
Created on 2015-7-28

@author: lingfeihua
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
                slow = slow.next
        media = slow
        tail = fast
        
        self.reverseList(media.next)
        p1 = head
        p2 = tail
        print(p1.val, p2.val)
        ret = True
        while p1 != media.next and p2 is not None:
            if p1.val != p2.val:
                ret = False
                break
            p1 = p1.next
            p2 = p2.next
                
        self.reverseList(tail)
        print(ret)
        return ret
        
    def reverseList(self, head):
        cur_tmp = head
        pre_tmp = None
        while cur_tmp is not None:
            next_tmp = cur_tmp.next
            cur_tmp.next = pre_tmp
            pre_tmp = cur_tmp
            cur_tmp = next_tmp
head = ListNode(1)
head.next = ListNode(2)
sl = Solution()
sl.isPalindrome(head)