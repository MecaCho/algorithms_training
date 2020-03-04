
994. Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

994. 腐烂的橘子
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

 

示例 1：



输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 

提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2


```
class Solution(object):
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        rottens = [(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2]
        freshes = [(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1]
        time = 0
        new_rottens = rottens

        while freshes:
            if not new_rottens:
                return -1
            new_rottens = []
            for i, j in rottens:
                for new_i, new_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    local = (i + new_i, j + new_j)
                    if local in freshes:
                        new_rottens.append(local)
                        freshes.remove(local)
            rottens += new_rottens
            time += 1

        return time
```

作者：qiuwenqi
链接：https://leetcode-cn.com/problems/rotting-oranges/solution/bsf-python2-by-qiuwenqi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
