


'''
5180. 带限制的子序列和
给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。

数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。



示例 1：

输入：nums = [10,2,-10,5,20], k = 2
输出：37
解释：子序列为 [10, 2, 5, 20] 。
示例 2：

输入：nums = [-1,-2,-3], k = 1
输出：-1
解释：子序列必须是非空的，所以我们选择最大的数字。
示例 3：

输入：nums = [10,-2,-10,-5,20], k = 2
输出：23
解释：子序列为 [10, -2, -5, 20] 。


提示：

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

5180. Constrained Subset Sum
Given an integer array nums and an integer k, return the maximum sum of a non-empty subset of that array such that for every two consecutive integers in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subset of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.



Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subset is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subset must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subset is [10, -2, -5, 20].


Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''


class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]

        dp[0] = nums[0]
        q = [nums[0]]
        res = nums[0]
        max_items = [nums[0]]
        for i in range(1, len(nums)):
            dp[i] = nums[i]

            dp[i] = max(dp[i], max_items[0] + nums[i])
            # for j in range(1, len(q)+1):
            # dp[i] = max(dp[i], dp[i-j]+nums[i])

            if len(q) >= k:
                rm_item = q.pop(0)
                if rm_item == max_items[0]:
                    max_items.pop(0)

            q.append(dp[i])
            while max_items and dp[i] > max_items[-1]:
                max_items.pop()

            max_items.append(dp[i])
            res = max(res, dp[i])

        return res
