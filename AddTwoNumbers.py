"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        pre = head
        l1_temp, l2_temp = l1, l2
        flag, val, val1, val2 = 0, 0, 0, 0
        while l1_temp or l2_temp:
            if not l1_temp:
                val1 = 0
            else:
                val1 = l1_temp.val
            if not l2_temp:
                val2 = 0
            else:
                val2 = l2_temp.val
            val = val1+val2+flag
            if val > 9:
                flag = val/10
                val %= 10
            else:
                flag = 0
            temp = ListNode(val)
            pre.next = temp
            pre = temp
            if l1_temp:
                l1_temp = l1_temp.next
            if l2_temp:
                l2_temp = l2_temp.next
        if flag:
            pre.next = ListNode(flag)
        return head.next
