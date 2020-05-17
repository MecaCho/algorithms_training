'''
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''

class Solution1(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i-1][j]
                elif i != 0 and j != 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1] if grid and grid[0] else None


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return None

        if not grid[0]:
            return sum(grid)
    
        dp = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                if j == 0 and i != 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
    
        print(dp)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                min_pre = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
                dp[i][j] = min(min_pre, dp[i][j])
        print(dp)
        return dp[-1][-1]


'''
概述
找出一条从左上角到右下角的路径，路径上数字之和最小。

题解
方法 1： 暴力
暴力就是利用递归，对于每个元素我们考虑两条路径，向右走和向下走，在这两条路径中挑选路径权值和较小的一个。

\mathrm{cost}(i, j)=\mathrm{grid}[i][j] + \min \big(\mathrm{cost}(i+1, j), \mathrm{cost}(i, j+1) \big)
cost(i,j)=grid[i][j]+min(cost(i+1,j),cost(i,j+1))

Java
public class Solution {
    public int calculate(int[][] grid, int i, int j) {
        if (i == grid.length || j == grid[0].length) return Integer.MAX_VALUE;
        if (i == grid.length - 1 && j == grid[0].length - 1) return grid[i][j];
        return grid[i][j] + Math.min(calculate(grid, i + 1, j), calculate(grid, i, j + 1));
    }
    public int minPathSum(int[][] grid) {
        return calculate(grid, 0, 0);
    }
}
复杂度分析

时间复杂度 ：O\big(2^{m+n}\big)O(2 
m+n
 )。每次移动最多可以有两种选择。
空间复杂度 ：O(m+n)O(m+n)。递归的深度是 m+nm+n。
方法 2：二维动态规划
算法

我们新建一个额外的 dpdp 数组，与原矩阵大小相同。在这个矩阵中，dp(i, j)dp(i,j) 表示从坐标 (i, j)(i,j) 到右下角的最小路径权值。我们初始化右下角的 dpdp 值为对应的原矩阵值，然后去填整个矩阵，对于每个元素考虑移动到右边或者下面，因此获得最小路径和我们有如下递推公式：

dp(i, j)= \mathrm{grid}(i,j)+\min\big(dp(i+1,j),dp(i,j+1)\big)
dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))

注意边界情况。下图描述了这个过程：


1 / 17

Java
public class Solution {
    public int minPathSum(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];
        for (int i = grid.length - 1; i >= 0; i--) {
            for (int j = grid[0].length - 1; j >= 0; j--) {
                if(i == grid.length - 1 && j != grid[0].length - 1)
                    dp[i][j] = grid[i][j] +  dp[i][j + 1];
                else if(j == grid[0].length - 1 && i != grid.length - 1)
                    dp[i][j] = grid[i][j] + dp[i + 1][j];
                else if(j != grid[0].length - 1 && i != grid.length - 1)
                    dp[i][j] = grid[i][j] + Math.min(dp[i + 1][j], dp[i][j + 1]);
                else
                    dp[i][j] = grid[i][j];
            }
        }
        return dp[0][0];
    }
}
复杂度分析

时间复杂度 ：O(mn)O(mn)。遍历整个矩阵恰好一次。
空间复杂度 ：O(mn)O(mn)。额外的一个同大小矩阵。
方法 3：一维动态规划
算法

在上个解法中，我们可以用一个一维数组来代替二维数组，dpdp 数组的大小和行大小相同。这是因为对于某个固定状态，只需要考虑下方和右侧的节点。首先初始化 dpdp 数组最后一个元素是右下角的元素值，然后我们向左移更新每个 dp(j)dp(j) 为：

dp(j)=\mathrm{grid}(i,j)+\min\big(dp(j),dp(j+1)\big)
dp(j)=grid(i,j)+min(dp(j),dp(j+1))

我们对于每一行都重复这个过程，然后向上一行移动，计算完成后 dp(0)dp(0) 就是最后的结果。

Java
public class Solution {
   public int minPathSum(int[][] grid) {
       int[] dp = new int[grid[0].length];
       for (int i = grid.length - 1; i >= 0; i--) {
           for (int j = grid[0].length - 1; j >= 0; j--) {
               if(i == grid.length - 1 && j != grid[0].length - 1)
                   dp[j] = grid[i][j] +  dp[j + 1];
               else if(j == grid[0].length - 1 && i != grid.length - 1)
                   dp[j] = grid[i][j] + dp[j];
               else if(j != grid[0].length - 1 && i != grid.length - 1)
                   dp[j] = grid[i][j] + Math.min(dp[j], dp[j + 1]);
               else
                   dp[j] = grid[i][j];
           }
       }
       return dp[0];
   }
}
复杂度分析

时间复杂度 ：O(mn)O(mn)。遍历整个矩阵恰好一次。
空间复杂度 ：O(n)O(n)。额外的一维数组，和一行大小相同。
方法 4：动态规划（不需要额外存储空间）
算法

和方法 2 相同，惟一的区别是，不需要用额外的 dpdp 数组，而是在原数组上存储，这样就不需要额外的存储空间。递推公式如下：

\mathrm{grid}(i, j)=\mathrm{grid}(i,j)+\min \big(\mathrm{grid}(i+1,j), \mathrm{grid}(i,j+1)\big)
grid(i,j)=grid(i,j)+min(grid(i+1,j),grid(i,j+1))

Java
public class Solution {
    public int minPathSum(int[][] grid) {
        for (int i = grid.length - 1; i >= 0; i--) {
            for (int j = grid[0].length - 1; j >= 0; j--) {
                if(i == grid.length - 1 && j != grid[0].length - 1)
                    grid[i][j] = grid[i][j] +  grid[i][j + 1];
                else if(j == grid[0].length - 1 && i != grid.length - 1)
                    grid[i][j] = grid[i][j] + grid[i + 1][j];
                else if(j != grid[0].length - 1 && i != grid.length - 1)
                    grid[i][j] = grid[i][j] + Math.min(grid[i + 1][j],grid[i][j + 1]);
            }
        }
        return grid[0][0];
    }
}
复杂度分析

时间复杂度 ：O(mn)O(mn)。遍历整个矩阵恰好一次。
空间复杂度 ：O(1)O(1)。不需要额外空间。

'''