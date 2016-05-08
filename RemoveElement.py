"""
	@Project: leetcode
	@file: RemoveElement.py
	@author: AC
	@time: 2016/5/8 23:51
	@Description: Given an array and a value, remove all instances of that value in place
	and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
    Example:
    Given input array nums = [3,2,2,3], val = 3
    Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i<length:
            if nums[i] == val:
                for j in xrange(i, length-1):
                    nums[j] = nums[j+1]
                length -= 1
            else:
                i += 1
        print length
        return nums[:length]

s = Solution()
print s.removeElement([3,2,2,3,2,3], 3)