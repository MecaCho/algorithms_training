'''
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4


221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        return maxSide ** 2
        # if not matrix or not matrix[0]:
        #     return 0
        # col_len = len(matrix)
        # row_len = len(matrix[0])
        # def get_square(i, j):

        #     res = 1
        #     l = min(col_len - i, row_len - j)
        #     for k in range(l):
        #         for ii in range(i, i+k+1):
        #             for jj in range(j, j+k+1):
        #                 if matrix[ii][jj] != "1":
        #                     # print(i, j, k)
        #                     return k

        #     # print(i, j, res, ii)
        #     # print(i, j, k, 1)
        #     return k


        # self.max_val = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         # print(matrix[i])
        #         if matrix[i][j] == "1":
        #             self.max_val = max(self.max_val, max(1, get_square(i, j)))
        # return self.max_val ** 2

'''
方法一：暴力法
由于正方形的面积等于边长的平方，因此要找到最大正方形的面积，首先需要找到最大正方形的边长，然后计算最大边长的平方即可。

暴力法是最简单直观的做法，具体做法如下：

遍历矩阵中的每个元素，每次遇到 11，则将该元素作为正方形的左上角；

确定正方形的左上角后，根据左上角所在的行和列计算可能的最大正方形的边长（正方形的范围不能超出矩阵的行数和列数），在该边长范围内寻找只包含 11 的最大正方形；

每次在下方新增一行以及在右方新增一列，判断新增的行和列是否满足所有元素都是 11。

JavaC++Python3Golang
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    # 遇到一个 1 作为正方形的左上角
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)
                    for k in range(1, currentMaxSide):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break
        
        maxSquare = maxSide * maxSide
        return maxSquare
复杂度分析

时间复杂度：O(mn \min(m,n)^2)O(mnmin(m,n) 
2
 )，其中 mm 和 nn 是矩阵的行数和列数。

需要遍历整个矩阵寻找每个 11，遍历矩阵的时间复杂度是 O(mn)O(mn)。
对于每个可能的正方形，其边长不超过 mm 和 nn 中的最小值，需要遍历该正方形中的每个元素判断是不是只包含 11，遍历正方形时间复杂度是 O(\min(m,n)^2)O(min(m,n) 
2
 )。
总时间复杂度是 O(mn \min(m,n)^2)O(mnmin(m,n) 
2
 )。
空间复杂度：O(1)O(1)。额外使用的空间复杂度为常数。

方法二：动态规划
方法一虽然直观，但是时间复杂度太高，有没有办法降低时间复杂度呢？

可以使用动态规划降低时间复杂度。我们用 dp(i, j)dp(i,j) 表示以 (i, j)(i,j) 为右下角，且只包含 11 的正方形的边长最大值。如果我们能计算出所有 dp(i, j)dp(i,j) 的值，那么其中的最大值即为矩阵中只包含 11 的正方形的边长最大值，其平方即为最大正方形的面积。

那么如何计算 dpdp 中的每个元素值呢？对于每个位置 (i, j)(i,j)，检查在矩阵中该位置的值：

如果该位置的值是 00，则 dp(i, j) = 0dp(i,j)=0，因为当前位置不可能在由 11 组成的正方形中；

如果该位置的值是 11，则 dp(i, j)dp(i,j) 的值由其上方、左方和左上方的三个相邻位置的 dpdp 值决定。具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 11，状态转移方程如下：

dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1
dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1

如果读者对这个状态转移方程感到不解，可以参考 1277. 统计全为 1 的正方形子矩阵的官方题解，其中给出了详细的证明。

此外，还需要考虑边界条件。如果 ii 和 jj 中至少有一个为 00，则以位置 (i, j)(i,j) 为右下角的最大正方形的边长只能是 11，因此 dp(i, j) = 1dp(i,j)=1。

以下用一个例子具体说明。原始矩阵如下。

0 1 1 1 0
1 1 1 1 0
0 1 1 1 1
0 1 1 1 1
0 0 1 1 1
对应的 dpdp 值如下。

0 1 1 1 0
1 1 2 2 0
0 1 2 3 1
0 1 2 3 2
0 0 1 2 3
下图也给出了计算 dpdp 值的过程。



JavaC++Python3Golang
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        maxSquare = maxSide * maxSide
        return maxSquare
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 和 nn 是矩阵的行数和列数。需要遍历原始矩阵中的每个元素计算 dp 的值。

空间复杂度：O(mn)O(mn)，其中 mm 和 nn 是矩阵的行数和列数。创建了一个和原始矩阵大小相同的矩阵 dp。由于状态转移方程中的 dp(i, j)dp(i,j) 由其上方、左方和左上方的三个相邻位置的 dpdp 值决定，因此可以使用两个一维数组进行状态转移，空间复杂度优化至 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''