"""
	@Project: leetcode
	@file: SwapNodesInPairs.py
	@author: AC
	@time: 2016/5/6 15:31
	@Description:	Given a linked list, swap every two adjacent nodes and return its head.
    For example, Given 1->2->3->4, you should return the list as 2->1->4->3.
    Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p, s, t = head, head, head.next
        new_head = head.next
        while t is not None and t.next is not None:
            s.next, t.next = t.next, s
            s = s.next
            t = s.next
            if t is not None:
                p.next = t
                p = s
        if t is not None and t.next is None:
            p.next = t
            t.next = s
            s.next = None
        return new_head