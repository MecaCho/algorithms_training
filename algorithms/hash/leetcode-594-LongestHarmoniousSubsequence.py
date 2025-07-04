# encoding=utf8

'''
594. Longest Harmonious Subsequence

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
 

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109

594. 最长和谐子序列

和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

给你一个整数数组 nums ，请你在所有可能的 子序列 中找到最长的和谐子序列的长度。

数组的 子序列 是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

 

示例 1：

输入：nums = [1,3,2,2,5,2,3,7]

输出：5

解释：

最长和谐子序列是 [3,2,2,2,3]。

示例 2：

输入：nums = [1,2,3,4]

输出：2

解释：

最长和谐子序列是 [1,2]，[2,3] 和 [3,4]，长度都为 2。

示例 3：

输入：nums = [1,1,1,1]

输出：0

解释：

不存在和谐子序列。

 

提示：

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
'''

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)

        res = [v + cnt[k+1] for k, v in cnt.items() if k + 1 in cnt]
        return max(res) if res else 0


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        res = 0
        for r,num in enumerate(nums):
            while num-nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                res = max(res, r-l+1)
        return res
