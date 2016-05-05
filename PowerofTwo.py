"""
	@Project: leetcode
	@file: PowerofTwo.py
	@author: AC
	@time: 2016/5/6 1:02
	@Description:	Given an integer, write a function to determine if it is a power of two.
"""
import time
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_int = 2**31
        if n<=0 or n>max_int:
            return False
        return max_int % n == 0

s = Solution()
print s.isPowerOfTwo(1)