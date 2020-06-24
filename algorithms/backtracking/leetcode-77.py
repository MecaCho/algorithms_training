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

        if k == 0:
            return [[]]

        res = []
        for i in range(k-1, n):
            for pre in self.combine(n-1, k-1):
                res.append(pre+[i+1])
        return res


        # self.vals = []
        # nums = [i +1 for i in range(n)]
        # def bk(path, start):
        #     # print(path, start, nums)
        #     if len(path) == k:
        #         self.vals.append(path)
        #         return
        #     for i in range(start, len(nums)):
        #         bk(path + [nums[i]], i+ 1)
        #
        # bk([], 0)
        # return self.vals


class Solution1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]

        res = []
        for i in range(1, n+1):
            for pre in self.combine(i-1, k-1):
                res.append(pre+[i])
        return res

if __name__ == '__main__':
    demo = Solution()
    res = demo.combine(4, 2)
    print(res)
