"""
	@Project: leetcode
	@file: Add Binary.py
	@author: AC
	@time: 2016/5/11
	@Description: Given two binary strings, return their sum (also a binary string).
    For example,
    a = "11"
    b = "1"
    Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))
        aa = ['0']*(max_len-len(a))+list(a)
        bb = ['0']*(max_len-len(b))+list(b)
        jinwei = 0
        result = []
        for i in xrange(max_len-1, -1, -1):
            temp = int(aa[i])+int(bb[i])+jinwei
            if temp >= 2:
                result.append(str(temp-2))
                jinwei = 1
            else:
                result.append(str(temp))
                jinwei = 0
        if jinwei == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)


s = Solution()
print s.addBinary('1', '1')