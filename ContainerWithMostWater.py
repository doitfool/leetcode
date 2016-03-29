# coding: utf-8
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""


class Solution(object):
    # 暴力超时
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in xrange(len(height)-1):
            for j in xrange(i+1, len(height)):
                area = (j-i)*min(height[j], height[i])
                print i, j, area
                if area > max_area:
                    max_area = area
        return max_area

if __name__ == '__main__':
    s = Solution()
    print s.maxArea([1, 2, 3, 4, 5])