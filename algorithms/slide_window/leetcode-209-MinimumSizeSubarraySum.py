'''
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。


209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        res = []
        cur_sum = 0
        cur = []
        while j < len(nums):
            cur_sum += nums[j]
            while cur_sum >= s:

                if not res or j - i + 1 < len(res):
                    res = nums[i: j +1]

                cur_sum -= nums[i]

                i += 1
            j += 1

        return len(res)


class Solution1(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        res = 0
        cur_sum = 0
        cur = []
        while j < len(nums):
            cur_sum += nums[j]
            while cur_sum >= s:
                if not res or j - i + 1 < res:
                    res = j - i + 1
                cur_sum -= nums[i]
                i += 1
            j += 1

        return res
