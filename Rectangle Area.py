"""
	@Project: leetcode
	@file: Rectangle Area.py
	@author: AC
	@time: 2016/5/12
	@Description:	Find the total area covered by two rectilinear rectangles in a 2D plane.
    Rectangle Area: Assume that the total area is never beyond the maximum possible value of int.
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_a = abs(A-C)*abs(B-D)
        area_b = abs(E-G)*abs(F-H)
        if C <= E or A >= G or D <= F or B >= H:
            area_ab = 0
        else:
            a = [A, C, E, G]
            b = [B, D, F, H]
            a.remove(max(a))
            a.remove(min(a))
            b.remove(max(b))
            b.remove(min(b))
            area_ab = abs(b[0]-b[1])*abs(a[0]-a[1])
        return area_a+area_b-area_ab
