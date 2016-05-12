"""
    @Project: leetcode
    @file: Word Pattern.py
    @author: AC
    @time: 16-5-12
    @Description:   Given a pattern and a string str, find if str follows the same pattern.
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
    Examples:
    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.
    Notes:
    You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        flag = True
        splits = str.strip().split(' ')
        lp, ls = len(pattern), len(splits)
        if lp != ls:
            flag = False
        else:
            dic = {}
            for i in xrange(lp):
                if splits[i] not in dic.keys():
                    if pattern[i] not in dic.values():
                        dic[splits[i]] = pattern[i]
                    else:
                        flag = False
                        break
                else:
                    if dic[splits[i]] != pattern[i]:
                        flag = False
                        break
        return flag