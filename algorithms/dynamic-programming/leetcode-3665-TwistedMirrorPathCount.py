# encoding=utf8

'''
3665. Twisted Mirror Path Count
Given an m x n binary grid grid where:

- grid[i][j] == 0 represents an empty cell, and
- grid[i][j] == 1 represents a mirror.

A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

- If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
- If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.

If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

Since the answer may be very large, return it modulo 10^9 + 7.

Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.



Example 1:

Input: grid = [[0,1,0],[0,0,1],[1,0,0]]
Output: 5
Explanation:
Number  Full Path
1       (0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
2       (0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
3       (0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
4       (0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
5       (0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
[M] indicates the robot attempted to enter a mirror cell and instead reflected.

Example 2:

Input: grid = [[0,0],[0,0]]
Output: 2
Explanation:
Number  Full Path
1       (0, 0) → (0, 1) → (1, 1)
2       (0, 0) → (1, 0) → (1, 1)

Example 3:

Input: grid = [[0,1,1],[1,1,0]]
Output: 1
Explanation:
Number  Full Path
1       (0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.



Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 500
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0


3665. 统计镜子反射路径数目
给你一个 m x n 的二进制网格 grid，其中：

- grid[i][j] == 0 表示一个空格子。
- grid[i][j] == 1 表示一面镜子。

一个机器人从网格的左上角 (0, 0) 出发，想要到达右下角 (m - 1, n - 1)。它只能向 右 或向 下 移动。如果机器人试图移入一个有镜子的格子，它会在进入该格子前被 反射：

- 如果它试图向 右 移动进入镜子，它会被转向 下 方，并移动到镜子正下方的格子里。
- 如果它试图向 下 移动进入镜子，它会被转向 右 方，并移动到镜子正右方的格子里。

如果这次反射会导致机器人移动到网格边界之外，则该路径被视为无效，不应被计数。

返回从 (0, 0) 到 (m - 1, n - 1) 不同的有效路径数量。

由于答案可能非常大，请将其返回对 10^9 + 7 取模 的结果。

注意：如果一次反射将机器人移动到一个有镜子的格子，机器人会立即再次被反射。这次反射的方向取决于它进入该镜子的方向：如果它是向右移动进入的，它将被转向下方；如果它是向下移动进入的，它将被转向右方。这个过程将一直持续，直到机器人到达终点、越界或者移动到一个空格子。



示例 1:

输入： grid = [[0,1,0],[0,0,1],[1,0,0]]
输出： 5
解释：
编号    完整路径
1       (0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
2       (0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
3       (0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
4       (0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
5       (0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
[M] 表示机器人试图进入一个有镜子的格子但被反射了。

示例 2:

输入： grid = [[0,0],[0,0]]
输出： 2
解释：
编号    完整路径
1       (0, 0) → (0, 1) → (1, 1)
2       (0, 0) → (1, 0) → (1, 1)

示例 3:

输入： grid = [[0,1,1],[1,1,0]]
输出： 1
解释：
编号    完整路径
1       (0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) 超出边界，因此是无效路径。



提示:

m == grid.length
n == grid[i].length
2 <= m, n <= 500
grid[i][j] 的值为 0 或 1。
grid[0][0] == grid[m - 1][n - 1] == 0
'''


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(grid[0])

        # 滚动数组：f[j][0] 表示向右离开列 j - 1（即进入列 j）的路径数
        # f[j][1] 表示向下离开当前单元格的路径数
        f = [[0, 0] for _ in range(n + 1)]
        # 初始化起点 (0, 0)：在起点处机器人可以向右或向下出发，虚拟上方流入量设为 1
        f[1] = [1, 1]

        for row in grid:
            for j, x in enumerate(row):
                r = f[j][0]       # 从左侧 (i, j - 1) 向右流入
                d = f[j + 1][1]   # 从上方 (i - 1, j) 向下流入
                if x == 0:
                    # 空格子：进入后可以自由选择向右或向下离开
                    s = (r + d) % MOD
                    f[j + 1] = [s, s]
                else:
                    # 镜子：向右流入的被反射向下，向下流入的被反射向右（发生方向交换）
                    f[j + 1] = [d, r]

        # 终点 (m - 1, n - 1) 是空格子，其向右或向下的出流量均等于到达该位置的总路径数
        return f[n][0]


# golang solution

'''
func uniquePaths(grid [][]int) int {
	const mod = 1_000_000_007
	n := len(grid[0])

	// f[j][0] 表示向右流出的路径数，f[j][1] 表示向下流出的路径数
	f := make([][2]int, n+1)
	f[1] = [2]int{1, 1}

	for _, row := range grid {
		for j, x := range row {
			r := f[j][0]     // 从左侧 (i, j - 1) 向右流入
			d := f[j+1][1]   // 从上方 (i - 1, j) 向下流入
			if x == 0 {
				// 空格子：流入量之和为到达该格子的路径数，可自由向右或向下离开
				s := (r + d) % mod
				f[j+1] = [2]int{s, s}
			} else {
				// 镜子：流入方向交换（右变下，下变右）
				f[j+1] = [2]int{d, r}
			}
		}
	}

	return f[n][0]
}
'''

# solutions

'''
思路和算法：
1. 问题转化与流动建模：
   - 机器人在网格中只能向右或向下移动。
   - 考虑流经每个单元格 (i, j) 的路径数量：
     * 从左侧相邻格 (i, j - 1) 向右流入 (i, j) 的路径数为 r；
     * 从上方相邻格 (i - 1, j) 向下流入 (i, j) 的路径数为 d。
   - 当路径试图进入单元格 (i, j) 时，根据该单元格类型分类讨论：
     * 若 grid[i][j] == 0（空格子）：
       机器人成功进入该格子。因为是空格子，机器人下一步可以自由选择向右移动或向下移动。
       到达该格子的总路径数为 (r + d) % MOD。
       因此，从该格子向右离开的路径数与向下离开的路径数均为 (r + d) % MOD。
     * 若 grid[i][j] == 1（镜子格子）：
       根据题目规则，试图向右移入镜子的路径会被反射转向下方，进入 (i + 1, j)；
       试图向下移入镜子的路径会被反射转向右方，进入 (i, j + 1)。
       换言之，向右流入的 r 最终变成向下流出 (i, j)，向下流入的 d 最终变成向右流出 (i, j)。
       镜子的本质就是将两个方向的流量进行【对调】（Swap）！
       即：out_right = d, out_down = r。
     * 若发生连环反射（连续镜子）：
       由于上述对调规律在每个镜子单元格局部自洽，连续通过多个镜子只是在对应网格节点上依次进行方向交换，无需显式模拟光线追踪，DP 自然处理了所有的连环反射情况！

2. 拓扑序与无环性证明：
   - 无论正常移动还是经过镜子反射，每一次流动都严格使得坐标和 i + j 增加 1：
     * 正常向右：(i, j) -> (i, j + 1)，和增加 1；
     * 正常向下：(i, j) -> (i + 1, j)，和增加 1；
     * 镜子反射向右：从 (i, j) 向右流出进入 (i, j + 1)，和增加 1；
     * 镜子反射向下：从 (i, j) 向下流出进入 (i + 1, j)，和增加 1。
   - 整个过程不存在任何向左或向上的移动，依赖关系是严格无环的（DAG），状态转移严格按照从上到下、从左到右即可完成。

3. 空间优化（滚动数组）：
   - 观察转移方程，计算当前行第 j 列时，仅依赖本行第 j - 1 列的结果（左侧流入 r）以及上一行第 j 列的结果（上方流入 d）。
   - 因此可以使用长度为 n + 1 的一维数组 f 进行空间优化，其中 f[j+1][0] 记录向右流出的路径数，f[j+1][1] 记录向下流出的路径数。
   - 起点 (0, 0) 初始化为 f[1] = [1, 1]，即初始存在 1 条路径可向右或向下出发。
   - 终点 (m - 1, n - 1) 保证为 0（空格子），返回 f[n][0]（或 f[n][1]）即为到达终点的总有效路径数。

复杂度分析：
- 时间复杂度：O(m * n)，其中 m 和 n 分别是网格的行数和列数（2 <= m, n <= 500）。仅需双重循环遍历整个网格一次，每次状态转移只需常数次加法与赋值运算。
- 空间复杂度：O(n)，使用滚动数组优化后，空间复杂度从 O(m * n) 降低至 O(n)。
'''

