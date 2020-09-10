'''
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]


40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''



class Solution0(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.vals = []
        nums = sorted(candidates)
        def dfs(path, start, target):
            if target < 0:
                return
            # print(path, start)
            if target == 0:
                self.vals.append(path)
                return
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[i-1]:
                    dfs(path+[nums[i]], i+1, target - nums[i])
        dfs([], 0, target)
        return self.vals


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        candidates = sorted(candidates)
        def backtrack(pre, cur, target):
            # print(pre, cur, target)
            if target == 0 and cur not in self.res:
                self.res.append(cur)
            pre_c = None
            for i in range(pre, len(candidates)):
                if target - candidates[i] >= 0:
                    if pre_c is None or pre_c != candidates[i]:
                        pre_c = candidates[i]
                        backtrack(i+1, cur + [candidates[i]], target-candidates[i])

        backtrack(0, [], target)
        return self.res


class Solution1(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates = sorted(candidates)

        def get_towsum(target, cur):
            res = []
            hash_map = {}
            new_candidates = candidates[:]
            for c in cur:
                new_candidates.remove(c)
            for i in range(len(new_candidates)):
                num = new_candidates[i]
                new_two = sorted([num, target - num])
                if num in hash_map and new_two not in res:
                    res.append(new_two)
                hash_map[target - num] = num
            if target in new_candidates:
                res.append([target])
            return res

        candidates = sorted(candidates)

        def backtrack(pre, cur, target):
            if len(cur) > len(candidates) or target < candidates[0]:
                return
            new_twos = get_towsum(target, cur)
            if new_twos:
                for new_two in new_twos:
                    item = sorted(cur + new_two)
                    if item not in self.res:
                        self.res.append(item)
            for i in range(pre, len(candidates)):
                backtrack(i + 1, cur + [candidates[i]], target - candidates[i])

        backtrack(0, [], target)
        return self.res


class Solution20200910(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.vals = []
        candidates.sort()
        def bk(nums, sum_, start):
            if sum_ == target and nums not in self.vals:
                self.vals.append(nums)
            if sum_ > target or start >= len(candidates):
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                bk(nums+[num], sum_+num, i+1)

        bk([], 0, 0)
        return self.vals

    # 472 ms	12.8 MB	Python

class Solution202009101(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.vals = []
        candidates.sort()
        def bk(nums, sum_, start):
            if sum_ == target:
                self.vals.append(nums)
            if sum_ > target or start >= len(candidates):
                return

            for i in range(start, len(candidates)):
                if i == start or candidates[i] != candidates[i-1]:
                    num = candidates[i]
                    bk(nums+[num], sum_+num, i+1)

        bk([], 0, 0)
        return self.vals

    # 68 ms	12.7 MB	Python

# https://leetcode-cn.com/problems/combination-sum-ii/solution/combinationsum2-by-qiuwenqi/


