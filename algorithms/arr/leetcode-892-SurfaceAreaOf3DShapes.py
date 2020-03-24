'''
892. 三维形体的表面积
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

请你返回最终形体的表面积。

 

示例 1：

输入：[[2]]
输出：10
示例 2：

输入：[[1,2],[3,4]]
输出：34
示例 3：

输入：[[1,0],[0,2]]
输出：16
示例 4：

输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
示例 5：

输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
 

提示：

1 <= N <= 50
0 <= grid[i][j] <= 50

892. Surface Area of 3D Shapes
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
'''


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        if not grid:
            return res
        length = len(grid[0])

        def check(i, j):
            if i < 0 or j < 0 or i >= length or j >= length:
                return 0
            else:
                return grid[i][j]

        for i in range(length):
            for j in range(length):
                h = grid[i][j]
                if h:
                    res += 2
                    for add_i, add_j in [(0,1), (0,-1), (1,0), (-1, 0)]:
                        check_h = check(i+add_i, j+add_j)
                        if h > check_h:
                            res += (h - check_h)
        return res
