# encoding=utf8


'''

16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # res = target
        length = len(nums)
        if length <=3:
            return sum(nums)
            
        nums = sorted(nums)

        result_list = [nums[0] , nums[1] , nums[2]]
        closer = abs(nums[0] + nums[1] + nums[2] - target)
        for i in range(length):
            j = i + 1
            k = length - 1
            
            while j < k:
                new_sum = nums[i] + nums[j] + nums[k]
                if abs(new_sum - target) < closer:
                    closer = abs(new_sum - target)
                    result_list = [nums[i], nums[j], nums[k]]

                if new_sum - target == 0:
                    return sum([nums[i], nums[j], nums[k]])
                
                if new_sum - target > 0:
                    # if nums[k] > 0:
                    k -=1
                if new_sum - target < 0:
                    j += 1


        return sum(result_list)

