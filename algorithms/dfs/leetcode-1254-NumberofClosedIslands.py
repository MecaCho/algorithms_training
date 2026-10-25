# encoding=utf8

'''
1254. Number of Closed Islands
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <= 1


1254. 统计封闭岛屿的数目
二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

 

示例 1：

输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。

示例 2：

输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1

示例 3：

输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2

 

提示：

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <= 1
'''


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 0:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. 先将所有与矩阵四条边界相连的陆地（0）淹没为水（1）
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n - 1] == 0:
                dfs(i, n - 1)
        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m - 1][j] == 0:
                dfs(m - 1, j)

        # 2. 遍历矩阵内部，此时遇到的任何陆地（0）必定是完全封闭的岛屿
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)

        return ans


# golang solution

'''
func closedIsland(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])

	var dfs func(r, c int)
	dfs = func(r, c int) {
		if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 0 {
			return
		}
		grid[r][c] = 1
		dfs(r+1, c)
		dfs(r-1, c)
		dfs(r, c+1)
		dfs(r, c-1)
	}

	// 1. 先将与边界相连的陆地淹没
	for i := 0; i < m; i++ {
		if grid[i][0] == 0 {
			dfs(i, 0)
		}
		if grid[i][n-1] == 0 {
			dfs(i, n-1)
		}
	}
	for j := 0; j < n; j++ {
		if grid[0][j] == 0 {
			dfs(0, j)
		}
		if grid[m-1][j] == 0 {
			dfs(m-1, j)
		}
	}

	// 2. 统计内部所有未被淹没的封闭岛屿
	ans := 0
	for i := 1; i < m-1; i++ {
		for j := 1; j < n-1; j++ {
			if grid[i][j] == 0 {
				ans++
				dfs(i, j)
			}
		}
	}

	return ans
}
'''

# solutions

'''
思路和算法：
1. 问题本质：
   - 题目给定一个由 0（陆地）和 1（水域）构成的二维网格。
   - “封闭岛屿”是指上下左右四个方向完全被 1（水域）包围的连通陆地区块。
   - 显然，如果某个连通块中的任何一块陆地触碰到了网格的边界（即位于第 0 行、第 m - 1 行、第 0 列或第 n - 1 列），它就无法被完全包围（在网格之外没有水域将其阻隔），因此不可能是封闭岛屿。
   - 反之，只要一个陆地连通块不包含任何位于边界上的格子，它必定完全被内部或边界的水域所包围，因而一定是封闭岛屿。

2. 算法设计（逆向思维 / 先淹没边界）：
   - 第一阶段：遍历矩阵的四条外边界（顶行、底行、左列、右列）。
     * 若发现任何边界格子为陆地 0，从该位置启动 DFS / 洪水填充（Flood Fill），将所有与之连通的陆地格子就地修改为 1（淹没）。
     * 这一阶段清除了所有“不封闭”的陆地连通块。
   - 第二阶段：遍历矩阵内部（1 <= i < m - 1, 1 <= j < n - 1）。
     * 此时如果遇到 grid[i][j] == 0，说明找到了一座崭新的封闭岛屿，答案计数器 ans 加 1；
     * 同时从该位置启动 DFS 将整座岛屿淹没为 1，防止重复统计。
   - 最终返回 ans 即可。

复杂度分析：
- 时间复杂度：O(m * n)，其中 m 和 n 分别是网格的行数和列数。矩阵中的每个单元格至多被访问常数次，DFS 的总展开步数不超过单元格总数。
- 空间复杂度：O(m * n)，在最坏情况下（例如整个网格均为陆地），递归调用栈的深度可达到 O(m * n)。由于 m, n <= 100，栈深度最多为 10000，运行极为安全。
'''

