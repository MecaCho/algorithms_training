'''
378. 有序矩阵中第K小的元素
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

示例:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
说明:
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。

378. Kth Smallest Element in a Sorted Matrix
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''





class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def get_lower_nums(mid, row, col):
            i = row - 1
            j = 0
            cnt = 0
            while i >= 0 and j < col:
                if (matrix[i][j] <= mid):
                    cnt = cnt + i + 1
                    j+= 1
                else:
                    i -= 1
            return cnt
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        col_len = len(matrix)
        row_len = len(matrix[0])
        i = matrix[0][0]
        j = matrix[col_len-1][row_len - 1]
        while i <= j:
            mid = (i + j)/2
            nums = get_lower_nums(mid, row_len, col_len)
            if nums > k-1:
                j = mid - 1
            elif nums <= k-1:
                i = mid + 1
            # else:
            #     return mid
        return i
