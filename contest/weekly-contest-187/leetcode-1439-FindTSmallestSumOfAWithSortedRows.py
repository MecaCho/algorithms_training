'''
1439. 有序矩阵中的第 k 个最小数组和
给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。

你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。



示例 1：

输入：mat = [[1,3,11],[2,4,6]], k = 5
输出：7
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。
示例 2：

输入：mat = [[1,3,11],[2,4,6]], k = 9
输出：17
示例 3：

输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
输出：9
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。
示例 4：

输入：mat = [[1,1,10],[2,2,9]], k = 7
输出：12


提示：

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] 是一个非递减数组


1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.



Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12


Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.
'''


class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(mat)
        pre = [0]

        for i in range(n):
            cur = [a + b for a, b in itertools.product(pre, mat[i])]
            pre = heapq.nsmallest(min(k, len(cur)), cur)

        return pre[-1]

        # end = 0
        # for i in range(1, len(mat[0])+1):
        #     if i ** len(mat) >= k:
        #         end = i
        #         break
        # print(end)

        # self.vals = []
        # length = len(mat)
        # def backtrack(res, n):
        #     if n == length:
        #         self.vals.append(sum(res))
        #         # heapq.heappush(self.vals, sum(res))
        #     else:
        #         for j in range(0, end):
        #             # print(end, j)
        #             backtrack(res+[mat[n][j]], n+1)

        # backtrack([], 0)
        # print(sorted(self.vals))
        # # return sorted(self.vals, key=lambda x: sum(x))[k-1]
        # if k > len(self.vals):
        #     return 0
        # # print(heapq.nsmallest(k, self.vals))
        # return sorted(self.vals)[k-1]


        # steps = []
        # i = j =0
        # while i <= len(mat) and j <= len(mat[0]):
        #     i += 1
        #     j += 1
        #     steps.append(i*j)
        # for k in range(len(steps)):
        #     if k <= steps[k]:
        #         new_arr = [for i in mat[k]]




        # # for i in range(len(mat)):
        # #     for j in range(len(mat[0])):
        # #         steps.append((i+1)*(j+1))
        # print(steps)
        # return