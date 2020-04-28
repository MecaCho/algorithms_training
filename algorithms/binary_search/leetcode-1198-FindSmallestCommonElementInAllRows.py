'''
1198. 找出所有行中最小公共元素
给你一个矩阵 mat，其中每一行的元素都已经按 递增 顺序排好了。请你帮忙找出在所有这些行中 最小的公共元素。

如果矩阵中没有这样的公共元素，就请返回 -1。



示例：

输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
输出：5


提示：

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] 已按递增顺序排列。

1198. Find Smallest Common Element in All Rows
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.



Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5


Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.
'''





class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        hash_map = defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                hash_map[mat[i][j]] += 1
        for k, v in hash_map.items():
            if v == len(mat):
                return k
        return -1