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


class Solution0(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []

        def bk(res, start):
            # print(nums, res)
            self.vals.append(res)

            for i in range(start, len(nums)):
                bk(res + [nums[i]], i + 1)

        bk([], 0)

        return self.vals


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


class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            # print(res)
            res += [[i] + num for num in res]
        return res


class Solution20200920(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []
        length = len(nums)

        def bk(res, start):
            self.vals.append(res)
            for i in range(start, length):
                bk(res + [nums[i]], i + 1)

        bk([], 0)
        return self.vals


'''
解决方案
观察全排列/组合/子集问题，它们比较相似，且可以使用一些通用策略解决。

首先，它们的解空间非常大：

全排列：N!N!。

组合：N!N!。

子集：2^N2 
N
 ，每个元素都可能存在或不存在。

在它们的指数级解法中，要确保生成的结果 完整 且 无冗余，有三种常用的方法：

递归

回溯

基于二进制位掩码和对应位掩码之间的映射字典生成排列/组合/子集

相比前两种方法，第三种方法将每种情况都简化为二进制数，易于实现和验证。

此外，第三种方法具有最优的时间复杂度，可以生成按照字典顺序的输出结果。

方法一：递归
思路

开始假设输出子集为空，每一步都向子集添加新的整数，并生成新的子集。



PythonJava
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
复杂度分析

时间复杂度：\mathcal{O}(N \times 2^N)O(N×2 
N
 )，生成所有子集，并复制到输出结果中。

空间复杂度：\mathcal{O}(N \times 2^N)O(N×2 
N
 )，这是子集的数量。

对于给定的任意元素，它在子集中有两种情况，存在或者不存在（对应二进制中的 0 和 1）。因此，NN 个数字共有 2^N2 
N
  个子集。
方法二：回溯
算法

幂集是所有长度从 0 到 n 所有子集的组合。

根据定义，该问题可以看作是从序列中生成幂集。

遍历 子集长度，通过 回溯 生成所有给定长度的子集。



回溯法是一种探索所有潜在可能性找到解决方案的算法。如果当前方案不是正确的解决方案，或者不是最后一个正确的解决方案，则回溯法通过修改上一步的值继续寻找解决方案。



算法

定义一个回溯方法 backtrack(first, curr)，第一个参数为索引 first，第二个参数为当前子集 curr。

如果当前子集构造完成，将它添加到输出集合中。

否则，从 first 到 n 遍历索引 i。

将整数 nums[i] 添加到当前子集 curr。

继续向子集中添加整数：backtrack(i + 1, curr)。

从 curr 中删除 nums[i] 进行回溯。

PythonJava
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
复杂度分析

时间复杂度：\mathcal{O}(N \times 2^N)O(N×2 
N
 )，生成所有子集，并复制到输出集合中。

空间复杂度：\mathcal{O}(N \times 2^N)O(N×2 
N
 )，存储所有子集，共 nn 个元素，每个元素都有可能存在或者不存在。

方法三：字典排序（二进制排序） 子集
思路

该方法思路来自于 Donald E. Knuth。

将每个子集映射到长度为 n 的位掩码中，其中第 i 位掩码 nums[i] 为 1，表示第 i 个元素在子集中；如果第 i 位掩码 nums[i] 为 0，表示第 i 个元素不在子集中。



例如，位掩码 0..00（全 0）表示空子集，位掩码 1..11（全 1）表示输入数组 nums。

因此要生成所有子集，只需要生成从 0..00 到 1..11 的所有 n 位掩码。

乍看起来生成二进制数很简单，但如何处理左边填充 0 是一个问题。因为必须生成固定长度的位掩码：例如 001，而不是 1。因此可以使用一些位操作技巧：

PythonJava
nth_bit = 1 << n
for i in range(2**n):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i | nth_bit)[3:]
或者使用简单但低效的迭代进行控制：

PythonJava
for i in range(2**n, 2**(n + 1)):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i)[3:]
算法

生成所有长度为 n 的二进制位掩码。

将每个子集都映射到一个位掩码数：位掩码中第 i 位如果是 1 表示子集中存在 nums[i]，0 表示子集中不存在 nums[i]。

返回子集列表。

PythonJava
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output
复杂度分析

时间复杂度：\mathcal{O}(N \times 2^N)O(N×2 
N
 )，生成所有的子集，并复制到输出列表中。

空间复杂度：\mathcal{O}(N \times 2^N)O(N×2 
N
 )，存储所有子集，共 nn 个元素，每个元素都有可能存在或者不存在。

作者：LeetCode
链接：https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

思路:
思路一:库函数

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res
思路二:迭代

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
思路三:递归(回溯算法)

pythonjava
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res  
类似题目还有:

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
链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''