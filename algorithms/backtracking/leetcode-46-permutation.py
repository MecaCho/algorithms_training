'''
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''



class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.vals = []

        def backtrack(nums, res=None):
            if not nums:
                self.vals.append(res)
                return

            new_nums = nums[1:]
            val = nums[0]

            for i in range(len(res)+1):
                backtrack(new_nums, res[:i] + [val] + res[i:])

        backtrack(nums, res=[])
        return self.vals


import itertools

class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))


'''
思路：
思路1：库函数

Python3 itertools 文档

一行代码：

def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
思路 2：

回溯算法

代码：
PythonJava
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
类似题目还有：

39.组合总和

40. 组合总和 II

46. 全排列

47. 全排列 II

78. 子集

90. 子集 II

这类题目都是同一类型的,用回溯算法!

其实回溯算法关键在于:不合适就退回上一步

然后通过约束条件, 减少时间复杂度.

大家可以从下面的解法找出一点感觉!

78. 子集

class Solution:
	def subsets(self, nums):
        if not nums:
			return []
		res = []
		n = len(nums)

		def helper(idx, temp_list):
			res.append(temp_list)
			for i in range(idx, n):
				helper(i + 1, temp_list + [nums[i]])

		helper(0, [])
		return res
90. 子集 II

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        res = []
        nums.sort()
		# 思路1
        def helper1(idx, n, temp_list):
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx, n):
                helper1(i + 1, n, temp_list + [nums[i]])
		# 思路2
        def helper2(idx, n, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                if i > idx and  nums[i] == nums[i - 1]:
                    continue
                helper2(i + 1, n, temp_list + [nums[i]])

        helper2(0, n, [])
        return res
46. 全排列

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        res = []
        n = len(nums)
        visited = [0] * n
        def helper1(temp_list,length):
            if length == n:
                res.append(temp_list)
            for i in range(n):
                if visited[i] :
                    continue
                visited[i] = 1
                helper1(temp_list+[nums[i]],length+1)
                visited[i] = 0
        def helper2(nums,temp_list,length):
            if length == n:
                res.append(temp_list)
            for i in range(len(nums)):
                helper2(nums[:i]+nums[i+1:],temp_list+[nums[i]],length+1)
        helper1([],0)
        return res
47. 全排列 II

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
			return []
		nums.sort()
		n = len(nums)
		visited = [0] * n
		res = []

		def helper1(temp_list, length):
			# if length == n and temp_list not in res:
			# 	res.append(temp_list)
			if length == n:
				res.append(temp_list)
			for i in range(n):
				if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
					continue
				visited[i] = 1
				helper1(temp_list + [nums[i]], length + 1)
				visited[i] = 0

		def helper2(nums, temp_list, length):
			if length == n and temp_list not in res:
				res.append(temp_list)
			for i in range(len(nums)):
				helper2(nums[:i] + nums[i + 1:], temp_list + [nums[i]], length + 1)

		helper1([],0)
		# helper2(nums, [], 0)
		return res
39.组合总和

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        res = []

        def helper(candidates, target, temp_list):
            if target == 0:
                res.append(temp_list)
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                helper(candidates[i:], target - candidates[i], temp_list + [candidates[i]])
        helper(candidates,target,[])
        return res
40. 组合总和 II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j]  > target : break
                if j > i and candidates[j] == candidates[j-1]:continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
        backtrack(0, 0, [])
        return res

作者：powcai
链接：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''