# coding: utf-8
"""
    @Project: leetcode
    @file: Intersection of Two Linked Lists.py
    @author: AC
    @time: 16-5-12
    @Description: Write a program to find the node at which the intersection of two singly linked lists begins.
    For example, the following two linked lists:
        A:          a1 → a2
                           ↘
                             c1 → c2 → c3
                           ↗
        B:     b1 → b2 → b3
        begin to intersect at node c1.
    Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 超时
        # s = headA
        # result = None
        # while s:
        #     t = headB
        #     while t is not None and s != t:
        #         t = t.next
        #     if t is not None:
        #         result = t
        #         break
        #     else:
        #         s = s.next
        # return result
        result = None
        s, t = headA, headB
        la, lb = 0, 0
        while s:
            la += 1
            s = s.next
        while t:
            lb += 1
            t = t.next
        if la > lb:
            s, t = headA, headB
        else:
            s, t = headB, headA
        i = 0
        while i < abs(la-lb):
            s = s.next
            i += 1
        while s and t:
            if s == t:
                result = s
                break
            else:
                s = s.next
                t = t.next
        return result

