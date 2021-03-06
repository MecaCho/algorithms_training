'''

300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''


### 解题思路
# 此处撰写解题思路

### 代码

# 动态规划
class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp) if dp else 0

# 贪心+二分法
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > cur_nums[-1]:
                cur_nums.append(nums[i])
            else:
                l, r = 0, len(cur_nums) - 1
                while l <= r:
                    mid = (l + r) / 2
                    if cur_nums[mid] < nums[i]:
                        l = mid + 1
                    elif cur_nums[mid] > nums[i]:
                        r = mid - 1
                    else:
                        l = mid
                        break
                cur_nums[l] = nums[i]
        return len(cur_nums)