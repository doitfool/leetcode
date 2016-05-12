"""
    @Project: leetcode
    @file: Reverse Bits.py
    @author: AC
    @time: 16-5-12
    @Description:   Reverse bits of a given 32 bits unsigned integer.
    For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
    return 964176192 (represented in binary as 00111001011110000010100101000000).
    Follow up:
        If this function is called many times, how would you optimize it?
        Related problem: Reverse Integer
"""


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        data = []
        while n > 0:
            data.append(n % 2)
            n /= 2
        data = data+[0]*(32-len(data))
        result = 0
        for num in data:
            result = result*2 + num
        return result

s = Solution()
print s.reverseBits(43261596)