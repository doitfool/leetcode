"""
    @Project: leetcode
    @file: Remove Linked List Elements.py
    @author: AC
    @time: 16-5-12
    @Description:   Remove all elements from a linked list of integers that have value val.
    Example
    Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    Return: 1 --> 2 --> 3 --> 4 --> 5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        temp, pre = head.next, head
        while temp is not None:
            if temp.val == val:
                pre.next = temp.next
                temp = temp.next
            else:
                pre = pre.next
                temp = temp.next
        return head

nodes = []
nodes.append(ListNode(1))

s = Solution()
head = s.removeElements(nodes[0], 1)
temp = head
while temp is not None:
    print temp.val
    temp = temp.next
