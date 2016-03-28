"""
	@Project: leetcode
	@file: RegularExpressionMatching.py
	@author: AC
	@time: 2016/3/27 0:19
	@Description:   Implement regular expression matching with support for '.' and '*'.
"""

class Solution(object):
    def convert(self, s):
        t = []
        i = 0
        while i < len(s):
            c = s[i]
            count = 1
            i += 1
            while i < len(s) and s[i]==c:
                count += 1
                i += 1
            if i < len(s) and s[i]=='*':
                count = -1
                i += 1
            t.append((c, count))
        return t


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ss = self.convert(s)
        pp = self.convert(p)
        match = True
        for i in xrange(min(len(ss), len(pp))):
            print ss[i][0], ss[i][1], pp[i][0], pp[i][1]
            if ss[i][0] != pp[i][0]:
                if pp[i][0] != '.':
                    match = False
                    break
            elif ss[i][1] != pp[i][1]:
                if pp[i][1] != -1:
                    match = False
                    break
        return match

if __name__ == '__main__':
    s = Solution()
    print s.isMatch('aab', 'c*a*b*')