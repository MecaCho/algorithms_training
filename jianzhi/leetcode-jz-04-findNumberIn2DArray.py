




'''
面试题04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。



限制：

0 <= n <= 1000

0 <= m <= 1000



注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
'''

# best solution
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        col_len = len(matrix)
        row_len = len(matrix[0])
        i = 0
        j = row_len -1
        while i < col_len and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

# binary search
class Solution1(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # matrix = list(zip(matrix))
        if not matrix or not matrix[0]:
            return False
        col_len = len(matrix)
        row_len = len(matrix[0])

        def binary_find(arr):
            l,r  = 0, len(arr)-1
            while l <= r:
                mid = (l + r) / 2
                if target < arr[mid]:
                    r = mid - 1
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    return True
            return False


        for i in range(col_len):
            if matrix[i][row_len-1] >= target:
                res =  binary_find(matrix[i])
                if res:
                    return True
            else:
                continue
        return False

# violence solution
class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for nums in matrix:
            for num in nums:
                if num == target:
                    return True
        return False
