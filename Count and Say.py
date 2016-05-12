"""
    @Project: leetcode
    @file: Count and Say.py
    @author: AC
    @time: 16-5-12
    @Description:   The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence.

    Note: The sequence of integers will be represented as a string.
"""


class Solution(object):
    def cas(self, s):
        ss = []
        i, l = 0, len(s)
        while i < l:
            j = i
            while j < l and s[i] == s[j]:
                j += 1
            ss.append(str(j-i)+s[i])
            i = j
        return ''.join(ss)

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        while n > 1:
            result = self.cas(result)
            n -= 1
        return result

s = Solution()
for i in xrange(1, 10):
    print s.countAndSay(i)

