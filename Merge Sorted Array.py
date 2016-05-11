"""
	@Project: leetcode
	@file: Merge Sorted Array.py
	@author: AC
	@time: 2016/5/11
	@Description:Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
	sorted array.
    Note: You may assume that nums1 has enough space (size that is greater or equal to m + n)
    to hold additional elements from nums2. The number of elements initialized in nums1 and
    nums2 are m and n respectively.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j < n:
            while i<m+j and nums2[j] > nums1[i]:
                i += 1
            for k in xrange(m+j-1, i-1, -1):
                nums1[k+1] = nums1[k]
            nums1[i] = nums2[j]
            j += 1
            i += 1


s = Solution()
nums1, m, nums2, n = [1,1,3]+[0]*6, 3, [2,3,4,6,10], 5
s.merge(nums1, m, nums2, n)
print nums1[:m+n]



