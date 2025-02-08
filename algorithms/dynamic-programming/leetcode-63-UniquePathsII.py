# encoding=utf8

'''
63. Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) < 1 or len(obstacleGrid[0]) < 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    if i == 0:
                        if j == 0:
                            dp[0][0] = 1
                            continue
                        dp[0][j] = dp[0][j - 1]
                    elif j == 0:
                        dp[i][0] = dp[i - 1][0]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


# tips

'''
The robot can only move either down or right. Hence any cell in the first row can only be reached from the cell left to it. However, if any cell has an obstacle, you don't let that cell contribute to any path. So, for the first row, the number of ways will simply be
if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1] 
else
     obstacleGrid[i,j] = 0
You can do a similar processing for finding out the number of ways of reaching the cells in the first column.

For any other cell, we can find out the number of ways of reaching it, by making use of the number of ways of reaching the cell directly above it and the cell to the left of it in the grid. This is because these are the only two directions from which the robot can come to the current cell.

Since we are making use of pre-computed values along the iteration, this becomes a dynamic programming problem.
if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1]  + obstacleGrid[i - 1][j]
else
     obstacleGrid[i,j] = 0
'''

# solutions


'''
方法一：动态规划
思路和算法

我们用 f(i, j)f(i,j) 来表示从坐标 (0, 0)(0,0) 到坐标 (i, j)(i,j) 的路径总数，u(i, j)u(i,j) 表示坐标 (i, j)(i,j) 是否可行，如果坐标 (i, j)(i,j) 有障碍物，u(i, j) = 0u(i,j)=0，否则 u(i, j) = 1u(i,j)=1。

因为「机器人每次只能向下或者向右移动一步」，所以从坐标 (0, 0)(0,0) 到坐标 (i, j)(i,j) 的路径总数的值只取决于从坐标 (0, 0)(0,0) 到坐标 (i - 1, j)(i−1,j) 的路径总数和从坐标 (0, 0)(0,0) 到坐标 (i, j - 1)(i,j−1) 的路径总数，即 f(i, j)f(i,j) 只能通过 f(i - 1, j)f(i−1,j) 和 f(i, j - 1)f(i,j−1) 转移得到。当坐标 (i, j)(i,j) 本身有障碍的时候，任何路径都到到不了 f(i, j)f(i,j)，此时 f(i, j) = 0f(i,j)=0；下面我们来讨论坐标 (i, j)(i,j) 没有障碍的情况：如果坐标 (i - 1, j)(i−1,j) 没有障碍，那么就意味着从坐标 (i - 1, j)(i−1,j) 可以走到 (i, j)(i,j)，即 (i - 1, j)(i−1,j) 位置对 f(i, j)f(i,j) 的贡献为 f(i - 1, j)f(i−1,j)，同理，当坐标 (i, j - 1)(i,j−1) 没有障碍的时候，(i, j - 1)(i,j−1) 位置对 f(i, j)f(i,j) 的贡献为 f(i, j - 1)f(i,j−1)。综上所述，我们可以得到这样的动态规划转移方程：

f(i, j) = \left \{ \begin{aligned} 0 & , & u(i, j) = 0 \\ f(i - 1, j) + f(i, j - 1) & , & u(i, j) \neq 0 \end{aligned} \right.
f(i,j)={ 
0
f(i−1,j)+f(i,j−1)
​	
  
,
,
​	
  
u(i,j)=0
u(i,j) 

​	
 =0
​	
 

很显然我们可以给出一个时间复杂度 O(nm)O(nm) 并且空间复杂度也是 O(nm)O(nm) 的实现，由于这里 f(i, j)f(i,j) 只与 f(i - 1, j)f(i−1,j) 和 f(i, j - 1)f(i,j−1) 相关，我们可以运用「滚动数组思想」把空间复杂度优化称 O(m)O(m)。「滚动数组思想」是一种常见的动态规划优化方法，在我们的题目中已经多次使用到，例如「剑指 Offer 46. 把数字翻译成字符串」、「70. 爬楼梯」等，当我们定义的状态在动态规划的转移方程中只和某几个状态相关的时候，就可以考虑这种优化方法，目的是给空间复杂度「降维」。如果你还不知道什么是「滚动数组思想」，一定要查阅相关资料进行学习哦。

代码中给出了使用「滚动数组思想」优化后的实现。

回顾这道题，其实这类动态规划的题目在题库中也出现过多次，例如「221. 最大正方形」、「1162. 地图分析」等。他们都以二维坐标作为状态，大多数都可以使用滚动数组进行优化。如果我们熟悉这类问题，可以一眼看出这是一个动态规划问题。当我们不熟悉的时候，怎么想到用动态规划来解决这个问题呢？我们需要从问题本身出发，寻找一些有用的信息，例如本题中：

(i, j)(i,j) 位置只能从 (i - 1, j)(i−1,j) 和 (i, j - 1)(i,j−1) 走到，这样的条件就是在告诉我们这里转移是 「无后效性」 的，f(i, j)f(i,j) 和任何的 f(i', j')(i' > i, j' > j)f(i 
′
 ,j 
′
 )(i 
′
 >i,j 
′
 >j) 无关。
动态规划的题目分为两大类，一种是求最优解类，典型问题是背包问题，另一种就是计数类，比如这里的统计方案数的问题，它们都存在一定的递推性质。前者的递推性质还有一个名字，叫做 「最优子结构」 ——即当前问题的最优解取决于子问题的最优解，后者类似，当前问题的方案数取决于子问题的方案数。所以在遇到求方案数的问题时，我们可以往动态规划的方向考虑。
通常如果我们察觉到了这两点要素，这个问题八成可以用动态规划来解决。读者可以多多练习，熟能生巧。

代码

C++JavaGolangC

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    n, m := len(obstacleGrid), len(obstacleGrid[0])
    f := make([]int, m)
    if obstacleGrid[0][0] == 0 {
        f[0] = 1
    }
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if obstacleGrid[i][j] == 1 {
                f[j] = 0
                continue
            }
            if j - 1 >= 0 && obstacleGrid[i][j-1] == 0 {
                f[j] += f[j-1]
            }
        }
    }
    return f[len(f)-1]
}
复杂度分析

时间复杂度：O(nm)O(nm)，其中 nn 为网格的行数，mm 为网格的列数。我们只需要遍历所有网格一次即可。
空间复杂度：O(m)O(m)。利用滚动数组优化，我们可以只用 O(m)O(m) 大小的空间来记录当前行的 ff 值。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/unique-paths-ii/solution/bu-tong-lu-jing-ii-by-leetcode-solution-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
