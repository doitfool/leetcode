"""
    @Project: leetcode
    @file: Length of Last Word.py
    @author: AC
    @time: 16-5-12
    @Description:   Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
    return the length of last word in the string.
    If the last word does not exist, return 0.
    Note: A word is defined as a character sequence consists of non-space characters only.
    For example,  Given s = "Hello World", return 5.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        b_index = s.rfind(' ')
        print b_index
        return len(s)-1-b_index