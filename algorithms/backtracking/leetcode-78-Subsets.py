'''
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''






class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []
        def backtrack(pre, new_c, k):
            if k > len(nums):
                return
            if len(new_c) == k:
                self.vals.append(new_c)
            for i in range(pre, len(nums)):
                num = nums[i]
                if not new_c or num not in new_c:
                    backtrack(i+1, [num] + new_c, k+1)
        backtrack(0, [], 0)
        return self.vals
