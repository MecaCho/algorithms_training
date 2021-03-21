# encoding=utf8

'''
73. Set Matrix Zeroes
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？


示例 1：


输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
示例 2：


输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]


提示：

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''



class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cols = []
        rows = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.append(i)
                    rows.append(j)
        # print(cols, rows)
        for i in cols:
            matrix[i][:] = [0] * len(matrix[0])
        for j in rows:
            for k in range(len(matrix)):
                matrix[k][j] = 0
        return matrix


# solutions

'''
方法一：使用标记数组
思路和算法

我们可以用两个标记数组分别记录每一行和每一列是否有零出现。

具体地，我们首先遍历该数组一次，如果某个元素为 00，那么就将该元素所在的行和列所对应标记数组的位置置为 \text{true}true。最后我们再次遍历该数组，用标记数组更新原数组即可。

代码

C++JavaJavaScriptPython3GolangC

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 是矩阵的行数，nn 是矩阵的列数。我们至多只需要遍历该矩阵两次。

空间复杂度：O(m+n)O(m+n)，其中 mm 是矩阵的行数，nn 是矩阵的列数。我们需要分别记录每一行或每一列是否有零出现。

方法二：使用两个标记变量
思路和算法

我们可以用矩阵的第一行和第一列代替方法一中的两个标记数组，以达到 O(1)O(1) 的额外空间。但这样会导致原数组的第一行和第一列被修改，无法记录它们是否原本包含 00。因此我们需要额外使用两个标记变量分别记录第一行和第一列是否原本包含 00。

在实际代码中，我们首先预处理出两个标记变量，接着使用其他行与列去处理第一行与第一列，然后反过来使用第一行与第一列去更新其他行与列，最后使用两个标记变量更新第一行与第一列即可。

代码

C++JavaJavaScriptPython3GolangC

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 是矩阵的行数，nn 是矩阵的列数。我们至多只需要遍历该矩阵两次。

空间复杂度：O(1)O(1)，我们只需要常数空间存储若干变量。

方法三：使用一个标记变量
思路和算法

我们可以对方法二进一步优化，只使用一个标记变量记录第一列是否原本存在 00。这样，第一列的第一个元素即可以标记第一行是否出现 00。但为了防止第一列的第一个元素被提前更新，我们需要从最后一行开始，倒序地处理矩阵元素。

代码

C++JavaJavaScriptPython3GolangC

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 是矩阵的行数，nn 是矩阵的列数。我们至多只需要遍历该矩阵两次。

空间复杂度：O(1)O(1)，我们只需要常数空间存储若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/set-matrix-zeroes/solution/ju-zhen-zhi-ling-by-leetcode-solution-9ll7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
