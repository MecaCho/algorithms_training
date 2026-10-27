# encoding=utf8

'''
3963. Create Grid With Exactly One Path
You are given two integers m and n, representing the number of rows and columns of a grid.

Construct any m x n grid consisting only of the characters '.' and '#', where:

- '.' represents a free cell.
- '#' represents an obstacle cell.

A valid path is a sequence of free cells that:

- Starts at the top-left cell (0, 0).
- Ends at the bottom-right cell (m - 1, n - 1).
- Moves only:
  - Right, from (i, j) to (i, j + 1), or
  - Down, from (i, j) to (i + 1, j).

Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

 

Example 1:

Input: m = 2, n = 3
Output: ["..#","#.."]
Explanation:
The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)

Example 2:

Input: m = 3, n = 3
Output: ["..#","#..","##."]
Explanation:
The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)

Example 3:

Input: m = 1, n = 4
Output: ["...."]
Explanation:
The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)

 

Constraints:

1 <= m, n <= 25


3963. 构造恰好一条路径的网格
给你两个整数 m 和 n，分别表示网格的行数和列数。

请你构造 任意 一个只包含字符 '.' 和 '#' 的 m x n 网格，其中：

- '.' 表示空单元格。
- '#' 表示障碍物单元格。

有效路径 是满足以下条件的空单元格序列：

- 从左上角单元格 (0, 0) 开始。
- 在右下角单元格 (m - 1, n - 1) 结束。
- 只能向：
  - 右移动，从 (i, j) 到 (i, j + 1)，或者
  - 下移动，从 (i, j) 到 (i + 1, j)。

返回任意一个从左上角到右下角 恰好只有一条有效路径 的网格。

 

示例 1：

输入： m = 2, n = 3
输出： ["..#","#.."]
解释：
唯一的有效路径是：(0,0) → (0,1) → (1,1) → (1,2)

示例 2：

输入： m = 3, n = 3
输出： ["..#","#..","##."]
解释：
唯一的有效路径是：(0,0) → (0,1) → (1,1) → (1,2) → (2,2)

示例 3：

输入： m = 1, n = 4
输出： ["...."]
解释：
唯一的有效路径是：(0,0) → (0,1) → (0,2) → (0,3)

 

提示：

1 <= m, n <= 25
'''


class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        # 构造思路：
        # 将第一行全部设为空地 '.'，其余行的前 n - 1 列全部设为障碍 '#'，最后一列全部设为空地 '.'。
        # 这样从 (0, 0) 出发，只能沿着第一行一直向右走到 (0, n - 1)，然后只能沿着最后一列一直向下走到 (m - 1, n - 1)。
        # 路径唯一且合法。
        if m == 1:
            return ["." * n]
        return ["." * n] + ["#" * (n - 1) + "." for _ in range(m - 1)]


# golang solution

'''
func createGrid(m int, n int) []string {
	ans := make([]string, m)

	// 第一行全部填充 '.'
	firstRow := make([]byte, n)
	for j := 0; j < n; j++ {
		firstRow[j] = '.'
	}
	ans[0] = string(firstRow)

	// 其余各行前 n - 1 列填充 '#'，最后一列填充 '.'
	for i := 1; i < m; i++ {
		row := make([]byte, n)
		for j := 0; j < n-1; j++ {
			row[j] = '#'
		}
		row[n-1] = '.'
		ans[i] = string(row)
	}

	return ans
}
'''

# solutions

'''
思路和算法：
1. 题目目标：
   - 给定网格大小 m x n，要求构造一个仅包含 '.'（空地）和 '#'（障碍）的网格。
   - 只能向右或向下移动，从起点 (0, 0) 到终点 (m - 1, n - 1) 必须存在且仅存在一条有效路径。

2. 构造策略（折线路径隔离）：
   - 构造一条确定且唯一的通道，封闭其他所有可能的分支分支：
     * 将整个第 0 行的所有格子 (0, j) 全部设为空地 '.'（0 <= j < n）；
     * 将整个第 n - 1 列的所有格子 (i, n - 1) 全部设为空地 '.'（0 <= i < m）；
     * 其余所有格子（即 1 <= i < m 且 0 <= j < n - 1）全部设为障碍 '#'。
   - 路径唯一性证明：
     * 从 (0, 0) 出发：在第 0 行除 (0, n - 1) 外的任意格子 (0, j)（j < n - 1），其下方格子 (1, j) 均为障碍 '#'，因此在该位置无法向下移动，必须且只能向右移动；
     * 沿着第 0 行向右移动到达 (0, n - 1) 后，右方已到达边界，无法向右移动，只能沿着第 n - 1 列一直向下移动；
     * 在第 n - 1 列移动期间，只能继续向下移动直至到达目标单元格 (m - 1, n - 1)；
     * 不存在任何其他可以到达 (m - 1, n - 1) 的路径，路径条数严格为 1。

3. 边界情况：
   - 当 m = 1 时，整张网格只有 1 行，全部填充 '.' 即可，唯一路径即一直向右走；
   - 当 n = 1 时，整张网格只有 1 列，全部填充 '.' 即可，唯一路径即一直向下走；
   - 上述统一逻辑对 m = 1 或 n = 1 均完全自洽。

复杂度分析：
- 时间复杂度：O(m * n)，其中 m 和 n 分别是网格的行数和列数（m, n <= 25）。填充并生成长度为 m 的字符串数组，总字符数为 m * n，耗时微秒级。
- 空间复杂度：O(m * n)，用于存储返回的网格字符串数组结果。
'''

