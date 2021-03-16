# encoding=utf8

'''
59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20


59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。



示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]


提示：

1 <= n <= 20
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for j in range(n)] for i in range(n)]
        num = 1
        j = 0
        while num <= n * n:
            for right in range(j, n - j):
                res[j][right] = num
                num += 1
            for down in range(j + 1, n - j):
                res[down][n - j - 1] = num
                num += 1
            for left in range(n - j - 2, j - 1, -1):
                res[n - j - 1][left] = num
                num += 1
            for up in range(n - j - 2, j, -1):
                res[up][j] = num
                num += 1

            j += 1

        return res
