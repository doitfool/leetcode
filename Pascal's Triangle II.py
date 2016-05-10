"""
	@Project: leetcode
	@file: Pascal's Triangle II.py
	@author: AC
	@time: 2016/5/10
	@Description:	Given an index k, return the kth row of the Pascal's triangle.
    For example, given k = 3,
    Return [1,3,3,1].
    Note:
    Could you optimize your algorithm to use only O(k) extra space?
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex > 1:
            pre, j = [1, 1], 1
            while j < rowIndex:
                mid = [pre[i]+pre[i+1] for i in xrange(len(pre)-1)]
                pre = [1] + mid + [1]
                j += 1
            return pre

s = Solution()
for i in xrange(10):
    print s.getRow(i)