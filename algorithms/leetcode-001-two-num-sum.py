'''
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

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

# 双指针法
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hash_map = {}
        # for num in nums:
        #     if num in hash_map:
        #         return [hash_map[num], num]
        #     else:
        #         hash_map[target-num] = num
        # return []

        i, j = 0, len(nums) - 1
        while i < j:
            sum_ = nums[i] + nums[j]
            if sum_ > target:
                j -= 1
            elif sum_ < target:
                i += 1
            else:
                return [nums[i], nums[j]]
