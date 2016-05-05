"""
	@Project: leetcode
	@file: PowerofThree.py
	@author: AC
	@time: 2016/5/6 0:30
	@Description:
	    Given an integer, write a function to determine if it is a power of three.
        Follow up:
        Could you do it without using any loop / recursion?
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:  # 不要忘记
            return False
        while True:
            if n % 3 != 0:
                break
            else:
                n /= 3
        if n != 1:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfThree(-27)