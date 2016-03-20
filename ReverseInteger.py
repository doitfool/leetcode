"""
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        y = 0
        flag = True
        if x < 0:
            flag = False
            x = -x
        while x:
            y = 10*y + x % 10
            x /= 10
        if not flag:
            y = -y
        if y > 2**31-1 or y < -2**31:
            return 0
        return y
