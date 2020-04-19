'''
200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

200. 岛屿数量
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == "0":
                return 0
            else:
                # print(i, j, grid[i][j])
                res = 1
                grid[i][j] = "0"
                for add_i ,add_j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    # if grid[i + add_i][j + add_j]
                    res += dfs(i + add_i, j + add_j)
                # print(i, j, res)
                return res

        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j ]= ="1":
                    ans.append(dfs(i, j))

        # print(ans, grid)
        return len(ans)
