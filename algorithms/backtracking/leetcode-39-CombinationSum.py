'''
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution(object):
    def combinationSum(self, candidates, target):
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
            if target == 0:
                self.vals.append(path)
                return
            for i in range(start, len(nums)):
                dfs(path+[nums[i]], i, target - nums[i])
        dfs([], 0, target)
        return self.vals



class Solution0(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        # def split_num(target):
        #     hash_map = {}
        #     res = []
        #     for i in range(len(candidates)):
        #         hash_map[target-candidates[i]] = candidates[i]
        #         split_num()
        #         if candidates[i] in hash_map:
        #             res.append([candidates[i], target-candidates[i]])
        #     return res
        candidates = sorted(candidates)
        def get_towsum(target):
            res = []
            for i in range(len(candidates)):
                num = candidates[i]
                if (target - num) >= candidates[0]:
                    two_num = sorted([num, target-num])
                    if two_num not in res:
                        res.append(two_num)
            return res
        # min_c = min(candidates)
        def backtrack(cur):
            splited = False
            flag = True
            for i in range(len(cur)):
                if cur[i] not in candidates:
                    flag = False
                two_nums = get_towsum(cur[i])
                if two_nums:
                    splited = True
                    for two_num in two_nums:
                        backtrack(cur[:i] + two_num + cur[i+1:])
            if flag and sorted(cur) not in self.res:
                self.res.append(sorted(cur))
            if not splited:
                return

        backtrack(cur=[target])
        return self.res
