# encoding=utf8

'''
304. Range Sum Query 2D - Immutable
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.


304. 二维区域和检索 - 矩阵不可变
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。

Range Sum Query 2D
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。



示例：

给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12


提示：

你可以假设矩阵不可变。
会多次调用 sumRegion 方法。
你可以假设 row1 ≤ row2 且 col1 ≤ col2 。
'''



class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sums = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if i == 0:
                    self.sums[i][j] += self.sums[i][j-1] if j > 0 else 0
                elif j == 0:
                    self.sums[i][j] += self.sums[i-1][j]
                else:
                    self.sums[i][j] = self.sums[i-1][j] + self.sums[i][j-1] -  self.sums[i-1][j-1] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.sums[row2][col2]
        if row1 == 0:
            return self.sums[row2][col2] - self.sums[row2][col1-1]
        if col1 == 0:
            return self.sums[row2][col2] - self.sums[row1-1][col2]
        return self.sums[row2][col2] - self.sums[row1-1][col2] - self.sums[row2][col1-1] + self.sums[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# solutions


'''
前言
这道题是「303. 区域和检索 - 数组不可变」的进阶，第 303 题是在一维数组中做区域和检索，这道题是在二维矩阵中做区域和检索。

这道题有两种解法，分别是对每一行计算一维前缀和，以及对整个矩阵计算二维前缀和。

方法一：一维前缀和
第 303 题中，初始化时对数组计算前缀和，每次检索即可在 O(1)O(1) 的时间内得到结果。可以将第 303 题的做法应用于这道题，初始化时对矩阵的每一行计算前缀和，检索时对二维区域中的每一行计算子数组和，然后对每一行的子数组和计算总和。

具体实现方面，创建 mm 行 n+1n+1 列的二维数组 \textit{sums}sums，其中 mm 和 nn 分别是矩阵 \textit{matrix}matrix 的行数和列数，\textit{sums}[i]sums[i] 为 \textit{matrix}[i]matrix[i] 的前缀和数组。将 \textit{sums}sums 的列数设为 n+1n+1 的目的是为了方便计算每一行的子数组和，不需要对 \textit{col}_1=0col 
1
​	
 =0 的情况特殊处理。

JavaJavaScriptGolangPython3C++C

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i][j + 1] = _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        total = sum(_sums[i][col2 + 1] - _sums[i][col1] for i in range(row1, row2 + 1))
        return total
复杂度分析

时间复杂度：初始化 O(mn)O(mn)，每次检索 O(m)O(m)，其中 mm 和 nn 分别是矩阵 \textit{matrix}matrix 的行数和列数。
初始化需要遍历矩阵 \textit{matrix}matrix 计算二维前缀和，时间复杂度是 O(mn)O(mn)。
每次检索需要对二维区域中的每一行计算子数组和，二维区域的行数不超过 mm，计算每一行的子数组和的时间复杂度是 O(1)O(1)，因此每次检索的时间复杂度是 O(m)O(m)。

空间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是矩阵 \textit{matrix}matrix 的行数和列数。需要创建一个 mm 行 n+1n+1 列的前缀和数组 \textit{sums}sums。

方法二：二维前缀和
方法一虽然利用了前缀和，但是每次检索的时间复杂度是 O(m)O(m)，仍然没有降到 O(1)O(1)。为了将每次检索的时间复杂度降到 O(1)O(1)，需要使用二维前缀和，在初始化的时候计算二维前缀和数组。

假设 mm 和 nn 分别是矩阵 \textit{matrix}matrix 的行数和列数。定义当 0 \le i<m0≤i<m 且 0 \le j<n0≤j<n 时，f(i,j)f(i,j) 为矩阵 \textit{matrix}matrix 的以 (i,j)(i,j) 为右下角的子矩阵的元素之和：

f(i,j)=\sum\limits_{p=0}^i \sum\limits_{q=0}^j \textit{matrix}[p][q]
f(i,j)= 
p=0
∑
i
​	
  
q=0
∑
j
​	
 matrix[p][q]

当 i=0i=0 或 j=0j=0 时，计算 f(i,j)f(i,j) 只需要对矩阵 \textit{matrix}matrix 的最上边的行和最左边的列分别计算前缀和即可。当 ii 和 jj 都大于 00 时，如何计算 f(i,j)f(i,j) 的值？

当 ii 和 jj 都大于 00 时，假设计算 f(i,j)f(i,j) 时已经知道了 f(i-1,j)f(i−1,j)、f(i,j-1)f(i,j−1) 和 f(i-1,j-1)f(i−1,j−1) 的值。为了计算 f(i,j)f(i,j)，自然而然会想到使用 f(i-1,j)f(i−1,j)、f(i,j-1)f(i,j−1) 和 \textit{matrix}[i][j]matrix[i][j] 的值。

注意到 f(i-1,j)f(i−1,j) 和 f(i,j-1)f(i,j−1) 这两项涉及到的矩阵 \textit{matrix}matrix 的元素有重合，矩阵 \textit{matrix}matrix 的以 (i-1,j-1)(i−1,j−1) 为右下角的子矩阵都在这两项中出现。因此如果计算 f(i-1,j)+f(i,j-1)+\textit{matrix}[i][j]f(i−1,j)+f(i,j−1)+matrix[i][j]，则该结果值比 f(i,j)f(i,j) 多了 f(i-1,j-1)f(i−1,j−1)，因此 f(i,j)f(i,j) 的计算如下：

f(i,j)=f(i-1,j)+f(i,j-1)-f(i-1,j-1)+\textit{matrix}[i][j]
f(i,j)=f(i−1,j)+f(i,j−1)−f(i−1,j−1)+matrix[i][j]

具体推导如下：

\begin{aligned} &\quad \ f(i,j) \\ &=\sum\limits_{p=0}^{i-1} \sum\limits_{q=0}^{j-1} \textit{matrix}[p][q]+\sum\limits_{p=0}^{i-1} \textit{matrix}[p][j]+\sum\limits_{q=0}^{j-1} \textit{matrix}[i][q]+\textit{matrix}[i][j] \\ &=\Big(\sum\limits_{p=0}^{i-1} \sum\limits_{q=0}^{j-1} \textit{matrix}[p][q]+\sum\limits_{p=0}^{i-1} \textit{matrix}[p][j]\Big) \\ &\quad+\Big(\sum\limits_{p=0}^{i-1} \sum\limits_{q=0}^{j-1} \textit{matrix}[p][q]+\sum\limits_{q=0}^{j-1} \textit{matrix}[i][q]\Big) \\ &\quad-\sum\limits_{p=0}^{i-1} \sum\limits_{q=0}^{j-1} \textit{matrix}[p][q] \\ &\quad+\textit{matrix}[i][j] \\ &=\sum\limits_{p=0}^{i-1} \sum\limits_{q=0}^j \textit{matrix}[p][q]+\sum\limits_{p=0}^i \sum\limits_{q=0}^{j-1} \textit{matrix}[p][q]-\sum\limits_{p=0}^{i-1} \sum\limits_{q=0}^{j-1} \textit{matrix}[p][q]+\textit{matrix}[i][j] \\ &=f(i-1,j)+f(i,j-1)-f(i-1,j-1)+\textit{matrix}[i][j] \end{aligned}
​	
因此在初始化的时候，即可对所有 0 \le i<m0≤i<m 和 0 \le j<n0≤j<n 计算得到 f(i,j)f(i,j) 的值。



检索时，应利用预处理得到的 ff 的值。当 \textit{row}_1=0row 
1
​	
 =0 且 \textit{col}_1=0col 
1
​	
 =0 时，\text{sumRegion}(\textit{row}_1,\textit{col}_1,\textit{row}_2,\textit{col}_2)=f(\textit{row}_2,\textit{col}_2)sumRegion(row 

​	
  时，\text{sumRegion}(\textit{row}_1,\textit{col}_1,\textit{row}_2,\textit{col}_2)sumRegion(row 
1
可以写成如下形式：

\begin{aligned} &\quad \ \text{sumRegion}(\textit{row}_1,\textit{col}_1,\textit{row}_2,\textit{col}_2) \\ &=\text{sumRegion}(0,0,\textit{row}_2,\textit{col}_2) \\ &\quad-\text{sumRegion}(0,\textit{col}_1,\textit{row}_1-1,\textit{col}_2) \\ &\quad-\text{sumRegion}(\textit{row}_1,0,\textit{row}_2,\textit{col}_1-1) \\ &\quad-\text{sumRegion}(0,0,\textit{row}_1-1,\textit{col}_1-1) \\ &=\text{sumRegion}(0,0,\textit{row}_2,\textit{col}_2) \\ &\quad-(\text{sumRegion}(0,\textit{col}_1,\textit{row}_1-1,\textit{col}_2)+\text{sumRegion}(0,0,\textit{row}_1-1,\textit{col}_1-1)) \\ &\quad-(\text{sumRegion}(\textit{row}_1,0,\textit{row}_2,\textit{col}_1-1)+\text{sumRegion}(0,0,\textit{row}_1-1,\textit{col}_1-1)) \\ &\quad-\text{sumRegion}(0,0,\textit{row}_1-1,\textit{col}_1-1) \\ &\quad+2 \times \text{sumRegion}(\textit{row}_1,0,\textit{row}_2,\textit{col}_1-1) \\ &=\text{sumRegion}(0,0,\textit{row}_2,\textit{col}_2) \\ &\quad-\text{sumRegion}(0,0,\textit{row}_1-1,\textit{col}_2) \\ &\quad-\text{sumRegion}(0,0,\textit{row}_2,\textit{col}_1-1) \\ &\quad+\text{sumRegion}(0,0,\textit{row}_1-1,\textit{col}_1-1) \\ &=f(\textit{row}_2,\textit{col}_2)-f(\textit{row}_1-1,\textit{col}_2)-f(\textit{row}_2,\textit{col}_1-1)+f(\textit{row}_1-1,\textit{col}_1-1) \end{aligned}
​

即可在 O(1)O(1) 时间内得到 \text{sumRegion}(\textit{row}_1,\textit{col}_1,\textit{row}_2,\textit{col}_2)sumRegion(row 
 的值。

具体实现方面，创建 m+1m+1 行 n+1n+1 列的二维数组 \textit{sums}sums，其中 \textit{sums}[i+1][j+1]sums[i+1][j+1] 的值为上述 f(i,j)f(i,j) 的值。

将 \textit{sums}sums 的行数和列数分别设为 m+1m+1 和 n+1n+1 的目的是为了方便计算 \text{sumRegion}(\textit{row}_1,\textit{col}_1,\textit{row}_2,\textit{col}_2)sumRegion(row 
1
​	
 ,col 
1
​	
 ,row 
2
​	
 ,col 
2
​	
 ) ，不需要对 \textit{row}_1=0row 
1
​	
 =0 和 \textit{col}_1=0col 
1
​	
 =0 的情况特殊处理。此时有：

\begin{aligned} &\quad \ \text{sumRegion}(\textit{row}_1,\textit{col}_1,\textit{row}_2,\textit{col}_2) \\ &=\textit{sums}[\textit{row}_2+1][\textit{col}_2+1]-\textit{sums}[\textit{row}_1][\textit{col}_2+1]-\textit{sums}[\textit{row}_2+1][\textit{col}_1]+\textit{sums}[\textit{row}_1][\textit{col}_1] \end{aligned}

​	
 

JavaJavaScriptGolangPython3C++C

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i + 1][j + 1] = _sums[i][j + 1] + _sums[i + 1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]
复杂度分析

时间复杂度：初始化 O(mn)O(mn)，每次检索 O(1)O(1)，其中 mm 和 nn 分别是矩阵 \textit{matrix}matrix 的行数和列数。
初始化需要遍历矩阵 \textit{matrix}matrix 计算二维前缀和，时间复杂度是 O(mn)O(mn)。
每次检索的时间复杂度是 O(1)O(1)。

空间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是矩阵 \textit{matrix}matrix 的行数和列数。需要创建一个 m+1m+1 行 n+1n+1 列的二维前缀和数组 \textit{sums}sums。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable/solution/er-wei-qu-yu-he-jian-suo-ju-zhen-bu-ke-b-2z5n/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
