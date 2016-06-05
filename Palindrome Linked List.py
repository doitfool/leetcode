# coding: utf-8
"""
    @Project: leetcode
    @file: Palindrome Linked List.py
    @author: AC
    @time: 16-6-5
    @Description:
    Given a singly linked list, determine if it is a palindrome.

    Follow up:
    Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 异或有问题 ???
# class Solution(object):
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         l = 0
#         temp = head
#         while temp is not None:
#             l += 1
#             temp = temp.next
#         flag = 0
#         if l % 2 == 0:
#             temp = head
#             while temp is not None:
#                 flag ^= temp.val
#                 temp = temp.next
#         else:
#             temp = head
#             i = 0
#             while temp is not None:
#                 if i != l/2:
#                     flag ^= temp.val
#                 temp = temp.next
#                 i += 1
#         return True if flag == 0 else False

class Solution(object):
    def isPalindrome(self, head):
        temp = head
        data = []
        while temp is not None:
            data.append(temp.val)
            temp = temp.next
        l = len(data)
        flag = True
        for i in xrange(l/2):
            if data[i] != data[l-1-i]:
                flag = False
                break
        return flag

datas = [-31900,22571,-31634,19735,13748,16612,-28299,-16628,9614,-14444,-14444,9614,-16628,-31900,16612,13748,19735,-31634,22571,-28299]
listnodes = []
for data in datas:
    listnodes.append(ListNode(data))

for i in xrange(len(listnodes)-1):
    listnodes[i].next = listnodes[i+1]


s = Solution()
print s.isPalindrome(listnodes[0])