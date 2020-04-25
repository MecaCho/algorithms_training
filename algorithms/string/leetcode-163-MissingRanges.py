'''
163. 缺失的区间
给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

示例：

输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]

163. Missing Ranges
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''




class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        def get_range(n, m):
            if m - n == 2:
                return str(m-1)
            return str(n+1) + "->" + str(m-1)
        if not nums:
            return [get_range(lower-1, upper+1)]
        if lower < nums[0]:
            nums = [lower-1] + nums
        if upper > nums[-1]:
            nums.append(upper+1)
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                res.append(get_range(nums[i-1], nums[i]))
        return res

