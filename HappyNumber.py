"""
	@Project: leetcode
	@file: HappyNumbers.py
	@author: AC
	@time: 2016/5/6 1:07
	@Description:	Write an algorithm to determine if a number is "happy".
    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of
    the squares of its digits, and repeat the process until the number equals 1
    (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        visited = [n]
        while n != 1:
            n = sum([int(c)**2 for c in str(n)])
            if n not in visited:
                visited.append(n)
            else:
                break
        if n == 1:
            return True
        else:
            return False