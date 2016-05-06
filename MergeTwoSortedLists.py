"""
	@Project: leetcode
	@file: MergeTwoSortedLists.py
	@author: AC
	@time: 2016/5/6 12:50
	@Description:	Merge two sorted linked lists and return it as a new list. The new list should be made by splicing
	together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s, t = l1, l2
        head = ListNode(0)
        temp = head
        while s is not None and t is not None:
            if s.val < t.val:
                temp.next = s
                s = s.next
            else:
                temp.next = t
                t = t.next
            temp = temp.next
        while s is not None:
            temp.next = s
            s = s.next
            temp = temp.next
        while t is not None:
            temp.next = t
            t = t.next
            temp = temp.next
        return head.next