"""
	@Project: leetcode
	@file: FactorialTrailingZeroes.py
	@author: AC
	@time: 2016/5/9
	@Description:	Given an integer n, return the number of trailing zeroes in n!.
	Note: Your solution should be in logarithmic time complexity.
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n>0:
            n/=5
            result += n
        return result

s = Solution()
print s.trailingZeroes(1808548329)