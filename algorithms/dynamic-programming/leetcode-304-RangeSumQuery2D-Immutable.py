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


