# coding: utf-8
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:
            f1, f2, time = 1, 2, 2
            while n-time > 0:
                f1, f2 = f2, f1+f2
                time += 1
            return f2

if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print s.climbStairs(i)