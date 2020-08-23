'''
5482. Detect Cycles in 2D Grid
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.



Example 1:



Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:



Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:



Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false


Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid consists only of lowercase English letters.

5482. 二维网格图中探测环
给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。

一个环是一条开始和结束于同一个格子的长度 大于等于 4 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。

同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到 (1, 1) 回到了上一次移动时的格子。

如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。



示例 1：



输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
输出：true
解释：如下图所示，有 2 个用不同颜色标出来的环：

示例 2：



输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
输出：true
解释：如下图所示，只有高亮所示的一个合法环：

示例 3：



输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
输出：false


提示：

m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid 只包含小写英文字母。
'''


class Solution(object):
    import sys
    sys.setrecursionlimit(100000000)

    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """

        adds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        visited = set()

        self.res = False

        def dfs(i, j, px, py):
            char = grid[i][j]
            if (i, j) in visited:
                self.res = True
                return
                # print(i, j, char, self.res, (px, py))
            visited.add((i, j))

            for add_i, add_j in adds:
                new_i, new_j = i + add_i, j + add_j
                # print(new_i, new_j, i, j)
                if new_i == px and new_j == py:
                    continue

                if new_i < m and new_i >= 0 and new_j < n and new_j >= 0 and grid[new_i][new_j] == char:
                    if self.res:
                        break
                    dfs(new_i, new_j, i, j)

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and not self.res:
                    dfs(i, j, -1, -1)

                if self.res:
                    return True

        return self.res
