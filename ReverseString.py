"""
    Write a function that takes a string as input and returns the string reversed.
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = []
        for i in xrange(len(s)-1, -1, -1):
            ss.append(s[i])
        return ''.join(ss)

if __name__ == '__main__':
    solution = Solution()
    print solution.reverseString('hello')