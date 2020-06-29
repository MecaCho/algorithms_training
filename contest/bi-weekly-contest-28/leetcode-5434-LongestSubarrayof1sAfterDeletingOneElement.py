'''
5434. 删掉一个元素以后全为 1 的最长子数组
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。



提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
示例 4：

输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4
示例 5：

输入：nums = [0,0,0]
输出：0


提示：

1 <= nums.length <= 10^5
nums[i] 要么是 0 要么是 1 。


5434. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0


Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''


# tips

'''
Maintain a sliding window where there is at most one zero on it.
'''


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = len(nums) - 1
        max_res = 0
        zero_index = []
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                zero_index.append(i)
                if len(zero_index) >= 2:
                    if zero_index[-1] - zero_index[-2] == 1:
                        cur = 0
                    else:
                        cur = i - zero_index[-2] - 1
                else:
                    cur = cur
            max_res = max(max_res, cur)

        return min(max_res, max_length)

