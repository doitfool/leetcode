"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = {}
        i = 1
        for num in nums:
            if not dic.has_key(num):
                dic[num] = [i]
            else:
                dic[num].append(i)
            i += 1
        index1 = 0
        index2 = 0
        for num in nums:
            if dic.has_key(target-num):
                if num != target-num:
                    index1 = dic[num]
                    index2 = dic[target-num]
                else:
                    if len(dic[num])>=2:
                        index1 = dic[num][0]
                        index2 = dic[num][1]
                    else:
                        continue
                break
        if type(index1) is list:
            index1 = index1[0]
            index2 = index2[0]
        return index1, index2
