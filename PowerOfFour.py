"""
	@Project: leetcode
	@file: PowerOfFour.py
	@author: AC
	@time: 2016/5/9
	@Description:Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
    Example: Given num = 16, return true. Given num = 5, return false.
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num < 4:
            return False
        flag = True
        while num > 1:
            if num%4 != 0:
                flag = False
                break
            num /= 4
        return flag

s = Solution()
print s.isPowerOfFour(5)