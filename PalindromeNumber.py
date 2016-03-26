"""
	@Project: leetcode
	@file: PalindromeNumber.py
	@author: AC
	@time: 2016/3/26 23:11
	@Description:	Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        temp = x
        length = 0
        while temp > 0:
            temp /= 10
            length += 1
        temp, j, k, flag = x, length-1, 1, True
        while j >= k:
            head = temp/(10**j)%10
            tail = temp%(10**k) / (10**(k-1))
            if head != tail:
                flag = False
                break
            j -= 1
            k += 1
        return flag

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(12121)