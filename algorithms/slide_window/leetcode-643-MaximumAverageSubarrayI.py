# encoding=utf8


'''
643. Maximum Average Subarray I
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].


643. 子数组最大平均数 I
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。



示例：

输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


提示：

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
'''


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumK = sum(nums[:k])
        max_sum = sumK
        for i in range(k, len(nums)):
            sumK += nums[i]
            sumK -= nums[i-k]
            max_sum = max(max_sum, sumK)

        return float(max_sum)/k

