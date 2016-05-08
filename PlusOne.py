# coding: utf-8
"""
	@Project: leetcode
	@file: PlusOne.py
	@author: AC
	@time: 2016/5/9 0:21
	@Description:	Given a non-negative number represented as an array of digits, plus one to the number.
    The digits are stored such that the most significant digit is at the head of the list.
    大数加法[1,2,3,4]+1=[1,2,3,5]    [1,2,3,9]+1=[1,2,4,0]
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        jinwei = 1
        for i in xrange(len(digits)-1, -1, -1):
            temp = digits[i]+jinwei
            if temp >= 10:
                result.append(temp-10)
                jinwei = 1
            else:
                result.append(temp)
                jinwei = 0
        if jinwei > 0:
            result.append(jinwei)
        result.reverse()
        return result