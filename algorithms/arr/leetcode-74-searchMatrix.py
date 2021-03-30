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
方法一：两次二分查找
思路

由于每行的第一个元素大于前一行的最后一个元素，且每行元素是升序的，所以每行的第一个元素大于前一行的第一个元素，因此矩阵第一列的元素是升序的。

我们可以对矩阵的第一列的元素二分查找，找到最后一个不大于目标值的元素，然后在该元素所在行中二分查找目标值是否存在。

代码

C++JavaGolangJavaScriptC

func searchMatrix(matrix [][]int, target int) bool {
    row := sort.Search(len(matrix), func(i int) bool { return matrix[i][0] > target }) - 1
    if row < 0 {
        return false
    }
    col := sort.SearchInts(matrix[row], target)
    return col < len(matrix[row]) && matrix[row][col] == target
}
复杂度分析

时间复杂度：O(\log m+\log n)=O(\log mn)O(logm+logn)=O(logmn)，其中 mm 和 nn 分别是矩阵的行数和列数。

空间复杂度：O(1)O(1)。

方法二：一次二分查找
思路

若将矩阵每一行拼接在上一行的末尾，则会得到一个升序数组，我们可以在该数组上二分找到目标元素。

代码实现时，可以二分升序数组的下标，将其映射到原矩阵的行和列上。

代码

C++JavaGolangJavaScriptC

func searchMatrix(matrix [][]int, target int) bool {
    m, n := len(matrix), len(matrix[0])
    i := sort.Search(m*n, func(i int) bool { return matrix[i/n][i%n] >= target })
    return i < m*n && matrix[i/n][i%n] == target
}
复杂度分析

时间复杂度：O(\log mn)O(logmn)，其中 mm 和 nn 分别是矩阵的行数和列数。

空间复杂度：O(1)O(1)。

结语
两种方法殊途同归，都利用了二分查找，在二维矩阵上寻找目标值。值得注意的是，若二维数组中的一维数组的元素个数不一，方法二将会失效，而方法一则能正确处理。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/search-a-2d-matrix/solution/sou-suo-er-wei-ju-zhen-by-leetcode-solut-vxui/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
