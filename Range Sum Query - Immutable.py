# coding: utf-8
"""
	@Project: leetcode
	@file: Range Sum Query - Immutable.py
	@author: AC
	@time: 2016/5/13
	@Description: Given an integer array nums, find the sum of the elements between
	indices i and j (i ≤ j), inclusive.
    Example:
        Given nums = [-2, 0, 3, -5, 2, -1]
        sumRange(0, 2) -> 1
        sumRange(2, 5) -> -1
        sumRange(0, 5) -> -3
    Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.array = [0]
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            self.array.append(sum)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.array[j+1]-self.array[i]



# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1,2,3,4,5])
print numArray.sumRange(0, 1), numArray.sumRange(1, 2)