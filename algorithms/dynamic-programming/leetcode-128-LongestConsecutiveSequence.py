'''

128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''





class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        new_nums = sorted(set(nums))

        cur = [new_nums[0]]
        max_length = 1
        for i in range(1, len(new_nums)):
            if new_nums[i] == new_nums[i-1]+1:
                cur.append(nums[i])
                max_length = max(max_length, len(cur))
            else:
                cur = [nums[i]]
        return max_length
