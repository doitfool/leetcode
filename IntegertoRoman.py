"""
	@Project: leetcode
	@file: IntegertoRoman.py
	@author: AC
	@time: 2016/4/6 23:39
	@Description:	Given an integer, convert it to a roman numeral.
                    Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value = [1,   4,    5,   9,   10,  40,   50,  90,   100, 400,  500, 900,  1000]
        rom =  ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = len(value)-1
        temp = []
        while num > 0 and i >= 0:
            div = num / value[i]
            mod = num % value[i]
            for j in xrange(div):
                temp.append(rom[i])
            num = mod
            i -= 1
        result = ''.join(temp)
        return  result


if __name__ == '__main__':
    s = Solution()
    for i in xrange(1, 4000):
        print i, s.intToRoman(i)
