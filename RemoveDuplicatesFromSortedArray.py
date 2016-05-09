"""
	@Project: leetcode
	@file: RemoveDuplicatesFromSortedArray.py
	@author: AC
	@time: 2016/5/9
	@Description:	Given a sorted array, remove the duplicates in place such that each element appear
	only once and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    For example, Given input array nums = [1,1,2], Your function should return length = 2,
    with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 2:
            return l
        pre = 1
        for i in xrange(1, l):
            if nums[i-1] < nums[i]:
                nums[pre] = nums[i]
                pre += 1
        return pre

s = Solution()
nums = [1, 1, 2, 3, 3, 3, 5, 9]
result = s.removeDuplicates(nums)
print result, nums[:result]
