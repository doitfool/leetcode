# coding: utf-8

"""
    Project:    leetcode
    File:   LongestPalindromicSubstring
    Author: AC
    Date:   2016/3/23 22:16
    Description:       Given a string S, find the longest palindromic substring in S.
                       You may assume that the maximum length of S is 1000,
                       and there exists one unique longest palindromic substring.
"""


class Solution(object):
    def match(self, s):
        l = len(s)
        flag = True
        for i in xrange(l/2):
            if s[i] != s[l-i-1]:
                flag = False
                break
        return flag

    def longestPalindrome1(self, s):   # 暴力法超时
        """
        :type s: str
        :rtype: str
        """
        max, m, n = 0, 0, 0
        l = len(s)
        for i in xrange(l):
            for j in xrange(l):
                if j >= i:
                    temp = s[i:j+1]
                    if self.match(temp) and len(temp) > max:
                        max, m, n = len(temp), i, j
        return s[m:n+1]

    def longestPalindrome(self, s):
        l = len(s)
        if l <= 1:
            return s

        result = ''
        # 寻找奇数长度回文串的最大值，比如'aba'
        for i in xrange(1, l):
            low, high = i-1, i+1
            while low >= 0 and high < l and s[low] == s[high]:
                low -= 1
                high += 1
            sub = s[low+1:high]
            if len(sub) > len(result):
                result = sub
        # 寻找偶数长度回文串的最大值，比如'aa'
        for i in xrange(l):
            if i+1 < l and s[i] == s[i+1]:
                low, high = i-1, i+2
                while low >= 0 and high < l and s[low] == s[high]:
                    low -= 1
                    high += 1
                sub = s[low+1:high]
                if len(sub) > len(result):
                    result = sub
        return result


if __name__ == '__main__':
    c = Solution()
    print c.longestPalindrome('aa')