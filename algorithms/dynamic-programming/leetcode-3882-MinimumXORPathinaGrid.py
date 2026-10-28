# encoding=utf8

'''
3882. Minimum XOR Path in a Grid
You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

 

Example 1:

Input: grid = [[1,2],[3,4]]
Output: 6
Explanation:
There are two valid paths:
- (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
- (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
The minimum XOR value among all valid paths is 6.

Example 2:

Input: grid = [[6,7],[5,8]]
Output: 9
Explanation:
There are two valid paths:
- (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
- (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
The minimum XOR value among all valid paths is 9.

Example 3:

Input: grid = [[2,7,5]]
Output: 0
Explanation:
There is only one valid path:
- (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
The XOR value of this path is 0, which is the minimum possible.

 

Constraints:

1 <= m == grid.length <= 1000
1 <= n == grid[i].length <= 1000
m * n <= 1000
0 <= grid[i][j] <= 1023


3882. 网格图中最小异或路径
给你一个大小为 m * n 的二维整数数组 grid。

你从 左上角 的单元格 (0, 0) 出发，想要到达 右下角 的单元格 (m - 1, n - 1)。

在每一步中，你 可以 向右或向下 移动。

路径的 代价 定义为该路径上所有单元格（包括 起点和终点）的值的 按位异或。

返回从 (0, 0) 到 (m - 1, n - 1) 的所有有效路径中 最小 的可能异或值。

 

示例 1：

输入： grid = [[1,2],[3,4]]
输出： 6
解释：
有两条有效路径：
- (0, 0) → (0, 1) → (1, 1)，异或值为：1 XOR 2 XOR 4 = 7
- (0, 0) → (1, 0) → (1, 1)，异或值为：1 XOR 3 XOR 4 = 6
所有有效路径中的最小异或值为 6。

示例 2：

输入： grid = [[6,7],[5,8]]
输出： 9
解释：
有两条有效路径：
- (0, 0) → (0, 1) → (1, 1)，异或值为：6 XOR 7 XOR 8 = 9
- (0, 0) → (1, 0) → (1, 1)，异或值为：6 XOR 5 XOR 8 = 11
所有有效路径中的最小异或值为 9。

示例 3：

输入： grid = [[2,7,5]]
输出： 0
解释：
只有一条有效路径：
- (0, 0) → (0, 1) → (0, 2)，异或值为：2 XOR 7 XOR 5 = 0
这条路径的异或值为 0，这是可能达到的最小值。

 

提示：

1 <= m == grid.length <= 1000
1 <= n == grid[i].length <= 1000
m * n <= 1000
0 <= grid[i][j] <= 1023
'''


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j] 维护到达单元格 (i, j) 时所有可能的异或和集合
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                cur = set()
                # 从上方 (i - 1, j) 转移
                if i > 0:
                    for x in dp[i - 1][j]:
                        cur.add(x ^ val)
                # 从左方 (i, j - 1) 转移
                if j > 0:
                    for x in dp[i][j - 1]:
                        cur.add(x ^ val)
                dp[i][j] = cur

        return min(dp[m - 1][n - 1])


# golang solution

'''
func minCost(grid [][]int) int {
	m, n := len(grid), len(grid[0])

	// dp[i][j] 记录到达 (i, j) 处所有可达的异或值集合
	dp := make([][]map[int]struct{}, m)
	for i := range dp {
		dp[i] = make([]map[int]struct{}, n)
		for j := range dp[i] {
			dp[i][j] = make(map[int]struct{})
		}
	}

	dp[0][0][grid[0][0]] = struct{}{}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			val := grid[i][j]
			if i > 0 {
				for x := range dp[i-1][j] {
					dp[i][j][x^val] = struct{}{}
				}
			}
			if j > 0 {
				for x := range dp[i][j-1] {
					dp[i][j][x^val] = struct{}{}
				}
			}
		}
	}

	ans := 1024
	for x := range dp[m-1][n-1] {
		if x < ans {
			ans = x
		}
	}
	return ans
}
'''

# solutions

'''
思路和算法：
1. 异或运算的性质与最优子结构失效：
   - 常见的加权网格最短路 / 最小路径和问题满足贪心最优子结构（即在每个格子只需要保留当前的最小值）。
   - 但是按位异或运算（XOR）并不具备单调性，局部较大的异或值在后续与某个数字异或后可能变成更小的值（例如 7 ^ 7 = 0）。
   - 因此，不能仅记录到达每个格子的单个最小异或值，必须记录所有可能到达的异或和状态。

2. 约束条件分析与状态空间上限：
   - 题目关键限制：m * n <= 1000，且单元格的值范围为 0 <= grid[i][j] <= 1023（即不超过 10 位二进制数，2^10 = 1024）。
   - 若干个在 [0, 1023] 范围内的数字进行任意次异或运算，其结果依然严格保持在 [0, 1023] 之内。
   - 这意味着到达任意一个单元格 (i, j) 的可能异或值总数至多只有 1024 种！
   - 整体状态总数至多为 m * n * 1024 <= 1000 * 1024 ≈ 10^6，完全可以在时空限制内进行动态规划。

3. 动态规划设计：
   - 状态定义：dp[i][j] 表示从起点 (0, 0) 按照规则移动到达单元格 (i, j) 的所有可达路径异或值的集合。
   - 初始状态：起点 (0, 0) 的异或值只包含其自身值：dp[0][0] = {grid[0][0]}。
   - 状态转移：对于任意格子 (i, j)，只能从上方格子 (i - 1, j) 向下移动到达，或者从左方格子 (i, j - 1) 向右移动到达。
     * 若从上方到达：所有 x in dp[i - 1][j] 转移为 x ^ grid[i][j]；
     * 若从左方到达：所有 x in dp[i][j - 1] 转移为 x ^ grid[i][j]；
     * 合并上方和左方产生的所有新异或和，作为 dp[i][j] 的集合。
   - 最终答案：遍历到达终点 (m - 1, n - 1) 的异或集合 dp[m - 1][n - 1]，取其中的最小值 min(dp[m - 1][n - 1])。

复杂度分析：
- 时间复杂度：O(m * n * V)，其中 m * n <= 1000，V = 1024 为可能的异或值域上限。每个格子 (i, j) 的异或状态最多 1024 个，转移开销为 O(len(dp[i-1][j]) + len(dp[i][j-1])) <= O(V)。总运算次数在 10^6 级别，耗时数十毫秒。
- 空间复杂度：O(m * n * V)，需要存储每个网格的可达异或状态集合，总空间在几兆字节内，完全符合空间要求。
'''

