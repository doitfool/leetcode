"""
	@Project: leetcode
	@file: ReverseVowelsOfAString.py
	@author: AC
	@time: 2016/5/6 13:17
	@Description:
	Write a function that takes a string as input and reverse only the vowels of a string.
    Example 1:
    Given s = "hello", return "holle".
    Example 2:
    Given s = "leetcode", return "leotcede".
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = list(s)
        l, h = 0, len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l < h:
            while ss[l] not in vowels and l < h:
                l += 1
            while ss[h] not in vowels and h > l:
                h -= 1
            ss[l], ss[h] = ss[h], ss[l]
            l += 1
            h -= 1
        return ''.join(ss)

s = Solution()
print s.reverseVowels('aA')

