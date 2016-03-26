# coding: utf-8
"""
Implement atoi to convert a string to an integer.
整形范围：INT_MAX (2147483647) or INT_MIN (-2147483648)
leetcode python编译器的sys.maxint不是2147483647
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        maxint = 2147483647
        if str == None or len(str) < 1:
            return 0
        temp_str = str.strip()
        symbol = True
        if temp_str[0] == '-':
            symbol = False
            i = 1
        elif temp_str[0] == '+':
            i = 1
        else:
            i = 0
        result = 0
        while i < len(temp_str) and temp_str[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result = result*10 + int(temp_str[i])
            if result > maxint:
                break
            i += 1
        if symbol:
            if result > maxint:
                result = maxint
        else:
            if result > maxint+1:
                result = -(maxint+1)
            else:
                result = -result
        return result

