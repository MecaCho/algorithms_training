'''
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''



class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        # def backtrack(nums=None, new_per=None):
        #     print(nums, new_per)
        #     if not nums:
        #         # if len(new_per) == 2:
        #         self.res.append(new_per)
        #     else:
        #         val = nums[0]
        #         for i in range(len(new_per)+1):
        #             backtrack(nums[1:], new_per[:i+1]+ [val] + new_per[i+1:])
        # backtrack(nums[1:], [val] + new_per)
        def backtrack(pre, new_c):
            if len(new_c) == k:
                self.res.append(new_c)
            else:
                for i in range(pre, n):
                    num = i+ 1
                    if not new_c or num not in new_c:
                        backtrack(num, new_c + [num])

        ns = [i + 1 for i in range(n)]
        # for i in range()
        backtrack(0, [])

        return self.res
