# coding: utf-8
"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_value_dict = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        result, i = 0, 0
        while i < len(s):
            if s[i:i+2] in rom_value_dict:
                result += rom_value_dict[s[i:i+2]]
                i += 2
            elif s[i] in rom_value_dict:
                result += rom_value_dict[s[i]]
                i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('CMXVI')