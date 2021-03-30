# encoding=utf8


'''

74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

'''



class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(target, nums):
            i = 0
            j = len(nums) - 1
            while i <= j:
                mid = (i + j) / 2
                if target == nums[mid]:
                    return True
                elif target > nums[mid]:
                    i = mid + 1
                else:
                    j = mid - 1
            return False
        row_len = len(matrix)
        if row_len < 1:
            return False
        cow_len = len(matrix[0])
        if cow_len < 1:
            return False
        for i in range(row_len):
            if matrix[i][cow_len-1] > target:
                return binary_search(target, matrix[i])
            elif matrix[i][cow_len-1] < target:
                continue
            elif matrix[i][cow_len-1] == target:
                return True
        return False



class Solution20210320(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        loc_i, loc_j = 0, n - 1
        while loc_i < m and loc_j >= 0:
            loc_value = matrix[loc_i][loc_j]
            if loc_value == target:
                return True
            elif loc_value > target:
                loc_j -= 1
            else:
                loc_i += 1
        return False


# solutions

'''

'''
