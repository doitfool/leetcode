"""
	@Project: leetcode
	@file: Isomorphic Strings.py
	@author: AC
	@time: 2016/5/12
	@Description:	Given two strings s and t, determine if they are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
    For example,
    Given "egg", "add", return true.
    Given "foo", "bar", return false.
    Given "paper", "title", return true.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = True
        ls, lt = len(s), len(t)
        if ls != lt:
            flag = False
        else:
            dicst, dicts = {}, {}
            for i in xrange(ls):
                if s[i] not in dicst:
                    dicst[s[i]] = t[i]
                else:
                    if t[i] != dicst[s[i]]:
                        flag = False
                        break
                if t[i] not in dicts:
                    dicts[t[i]] = s[i]
                else:
                    if s[i] != dicts[t[i]]:
                        flag = False
                        break
        return flag