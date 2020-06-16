'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i, num in enumerate(nums):
            if num_dict.get(target - num) is not None:
                return num_dict[target - num], i
            num_dict[num] = i
        return None


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[target - nums[i]] = i
            else:
                return [hash_map[nums[i]], i]
