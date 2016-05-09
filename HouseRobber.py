"""
	@Project: leetcode
	@file: HouseRobber.py
	@author: AC
	@time: 2016/5/9 21:48
	@Description:	You are a professional robber planning to rob houses along a street. Each house has a certain
	amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent
	houses have security system connected and it will automatically contact the police if two adjacent
	houses were broken into on the same night.
    Given a list of non-negative integers representing the amount of money of each house,
    determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            rob_money = [nums[0], max(nums[0], nums[1])]
            for i in xrange(2, len(nums)):
                rob_money.append(max(rob_money[i-2]+nums[i], rob_money[i-1]))
            return rob_money[-1]


s = Solution()
print s.rob([1,4,2,6,3,1,5,2,9,1,4])

