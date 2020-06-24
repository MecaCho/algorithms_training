
'''
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = [[]]
        # for i in nums:
        #     # print(res)
        #     res += [[i] + num for num in res if i not in num]
        # return res

        self.vals = []
        nums = sorted(nums)
        def backtrack(pre, new_c, k):
            if k > len(nums):
                return
            if len(new_c) == k:
                # new_c = sorted(new_c)
                if new_c not in self.vals:
                    self.vals.append(new_c)
            for i in range(pre, len(nums)):
                backtrack(i+1, [nums[i]] + new_c, k+1)
        backtrack(0, [], 0)
        return self.vals


class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.vals = []
        nums.sort()

        def bk(res, start):
            self.vals.append(res)

            pre = None
            for i in range(start, len(nums)):
                if pre is None or pre != nums[i]:
                    bk(res + [nums[i]], i + 1)
                pre = nums[i]
        bk([], 0)
        return self.vals


class Solution2(object):
    def subsetsWithDup(self, nums):
        self.vals = []
        nums.sort()

        def bk(res, start):
            self.vals.append(res)

            for i in range(start, len(nums)):
                if i == start or nums[i - 1] != nums[i]:
                    bk(res + [nums[i]], i + 1)

        bk([], 0)

        return self.vals


if __name__ == '__main__':
    demo = Solution1()
    res = demo.subsetsWithDup([1,1,2,3])
    print(res)