"""
	@Project: leetcode
	@file: MoveZeroes.py
	@author: AC
	@time: 2016/5/4 0:58
	@Description:
		Given an array nums, write a function to move all 0's to the end of it
		while maintaining the relative order of the non-zero elements.
        For example, given nums = [0, 1, 0, 3, 12], after calling your function,
        nums should be [1, 3, 12, 0, 0].
    Note:
        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)-1):
            flag = True
            for j in xrange(len(nums)-1):
                if nums[j] == 0 and nums[j+1] != 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = False
            if flag:
                break

if __name__ == '__main__':
    s = Solution()
    nums = [0,2,0,1,23]
    s.moveZeroes(nums)
    print nums