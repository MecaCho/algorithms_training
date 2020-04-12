
'''
面试题57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]


限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''




class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return [hash_map[num], num]
            else:
                hash_map[target-num] = num
        return []


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

