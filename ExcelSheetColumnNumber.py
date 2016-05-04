"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = ['$']
        for i in xrange(1, 27):
            table.append(chr(ord('A')+(i-1)))
        result = 0
        l = len(s)
        for i in xrange(l):
            result += (26**(l-i-1))*table.index(s[i])
        print result
        return result

if __name__ == '__main__':
    s = Solution()
    s.titleToNumber('AAA')
