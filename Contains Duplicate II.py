"""
	@Project: leetcode
	@file: Contains Duplicate II.py
	@author: AC
	@time: 2016/5/12
	@Description:	Given an array of integers and an integer k, find out whether there are two distinct indices
	i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_idx, i = {}, 0
        while i < len(nums):
            if nums[i] not in num_idx:
                num_idx[nums[i]] = [i]
            else:
                num_idx[nums[i]].append(i)
            i += 1
        flag = False
        for key, v in num_idx.iteritems():
            if len(v) >= 2:
                temp = v
                for j in xrange(len(temp)-1):
                    if temp[j+1] - temp[j] <= k:
                        flag = True
                        break
            if flag:
                break
        return flag

s = Solution()
nums = [1,2,3,4,6,1]
k = 5
print s.containsNearbyDuplicate(nums, k)