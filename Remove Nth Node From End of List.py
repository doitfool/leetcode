"""
    @Project: leetcode
    @file: Remove Nth Node From End of List.py
    @author: AC
    @time: 16-5-12
    @Description:   Given a linked list, remove the nth node from the end of list and return its head.
    For example,
        Given linked list: 1->2->3->4->5, and n = 2.
        After removing the second node from the end, the linked list becomes 1->2->3->5.
    Note:
    Given n will always be valid.
    Try to do this in one pass.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        s, l = head, 0
        while s:
            l += 1
            s = s.next
        print l
        if n == l:
            return head.next

        s, i = head, 0
        while i < l-n-1:
            s = s.next
            i += 1
        if s.next is not None:
            s.next = s.next.next
        return head


nodes = []
nodes.append(ListNode(1))
nodes.append(ListNode(2))
nodes.append(ListNode(3))
nodes.append(ListNode(4))
nodes.append(ListNode(5))

nodes[0].next = nodes[1]
nodes[1].next = nodes[2]
nodes[2].next = nodes[3]
nodes[3].next = nodes[4]

s = Solution()
temp = s.removeNthFromEnd(nodes[0], 5)
while temp:
    print temp.val,
    temp = temp.next



