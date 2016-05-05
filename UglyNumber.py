"""
	@Project: leetcode
	@file: UglyNumber.py
	@author: AC
	@time: 2016/5/6 0:15
	@Description:	Write a program to check whether a given number is an ugly number.
                    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
                    For example, 6, 8 are ugly while 14 is not ugly since it includes
                    another prime factor 7.
                    Note that 1 is typically treated as an ugly number.
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while True:
            flag = True
            if num % 2 == 0:
                num /= 2
                flag = False
            if num % 3 == 0:
                num /= 3
                flag = False
            if num % 5 == 0:
                num /= 5
                flag = False
            if flag:
                break
        if num == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    for i in xrange(100):
        print i, s.isUgly(i)

