




'''
259. 较小的三数之和
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
进阶：是否能在 O(n2) 的时间复杂度内解决？

259. 3Sum Smaller
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
'''


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def tow_smaller(nums, target):
            res = 0
            i, j = 0, len(nums) - 1
            while i < j:
                sum = nums[i] + nums[j]
                if sum < target:
                    res += j - i
                    i += 1
                else:
                    j -= 1
            # print(res, target)
            return res

        res = 0
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            res += tow_smaller(nums[i + 1:], target - nums[i])

        return res
