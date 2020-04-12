'''

15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

15. 三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution(object):
    def twoSum(self, nums, target):
        tg_map = {}
        res = []
        for num in nums:
            if num in tg_map:
                res.append([num, target - num])
            else:
                tg_map[target - num] = num
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        res = []
        res_dict = {}
        if length < 3:
            return []
        if len(set(nums)) == 1:
            if nums[0] == 0:
                return [[0,0,0]]
            return []
        for i in range(length):
            j = i + 1
            target = 0 - nums[i]
            tg_list = self.twoSum(nums[j:], target)
            for tg in tg_list:
                new_ = sorted([nums[i], tg[0], tg[1]])
                key = "".join([str(x) for x in new_])
                res_dict[key] = new_
        for k, value in res_dict.items():
            res.append(value)

        return res

