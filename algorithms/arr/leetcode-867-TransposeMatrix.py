# encoding=utf8

'''
867. Transpose Matrix
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.





Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109



867. 转置矩阵
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。





示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：matrix = [[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
'''


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return map(list, zip(*matrix[:]))

# solutions


'''
方法一：模拟
如果矩阵 \textit{matrix}matrix 为 mm 行 nn 列，则转置后的矩阵 \textit{matrix}^\text{T}matrix 
T
  为 nn 行 mm 列，且对任意 0 \le i<m0≤i<m 和 0 \le j<n0≤j<n，都有 \textit{matrix}^\text{T}[j][i]=\textit{matrix}[i][j]matrix 
T
 [j][i]=matrix[i][j]。

创建一个 nn 行 mm 列的新矩阵，根据转置的规则对新矩阵中的每个元素赋值，则新矩阵为转置后的矩阵。

JavaJavaScriptGolangPython3Python3_onelineC++C

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是矩阵 \textit{matrix}matrix 的行数和列数。需要遍历整个矩阵，并对转置后的矩阵进行赋值操作。

空间复杂度：O(1)O(1)。除了返回值以外，额外使用的空间为常数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/transpose-matrix/solution/zhuan-zhi-ju-zhen-by-leetcode-solution-85s2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
