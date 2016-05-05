# coding: utf-8
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        pre, temp = head, head.next
        visited = [head.val]
        while temp is not None:
            if temp.val not in visited:
                visited.append(temp.val)
                temp = temp.next
                pre = pre.next
            else:
                pre.next = temp.next
                temp = temp.next
        return head