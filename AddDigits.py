"""
	@Project: leetcode
	@file: AddDigits.py
	@author: AC
	@time: 2016/5/3 23:33
	@Description:	Given a non-negative integer num, repeatedly add all its digits
	until the result has only one digit. For example: Given num = 38, the process is like:
	3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
	Could you do it without any loop/recursion in O(1) runtime?
	1~9     1~9
	10~18   1~9
	19~27   1~9
	28~36   1~9
	...     ...
"""


class Solution(object):
    # def addDigits(self, num):
    #     """
    #     :type num: int
    #     :rtype: int
    #     """
    #     temp = num
    #     while temp >= 10:
    #         temp = sum([int(c) for c in str(temp)])
    #     return temp
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0 :
            return 0
        else:
            return 1+(num-1)%9

if __name__ == '__main__':
    s = Solution()
    print s.addDigits(10)