"""
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxs = []
        sub = []
        max_temp = 0
        for c in s:
            if c not in sub:
                sub.append(c)
                max_temp += 1
            else:
                maxs.append(max_temp)
                sub = sub[sub.index(c)+1:]
                sub.append(c)
                max_temp = len(sub)
        maxs.append(max_temp)
        return max(maxs)
