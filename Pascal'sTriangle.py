"""
	@Project: leetcode
	@file: Pascal'sTriangle.py
	@author: AC
	@time: 2016/5/9 0:39
	@Description:	Given numRows, generate the first numRows of Pascal's triangle.
    For example, given numRows = 5,
    Return
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        else:
            result = [[1]]
            i, temp = 1, [0,1,0]
            while i<numRows:
                p1 = []
                for j in xrange(len(temp)-1):
                    p1.append(temp[j]+temp[j+1])
                result.append(p1)
                i += 1
                temp = [0]+p1+[0]
            return result