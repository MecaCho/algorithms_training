#encoding=UTF8

'''
1139. 最大的以 1 为边界的正方形
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。



示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
示例 2：

输入：grid = [[1,1,0,0]]
输出：1


提示：

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1


1139. Largest 1-Bordered Square
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.



Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1


Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
'''


class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_val = 0
        def check_square(i, j, v):
            if i + v >= len(grid) or j + v >= len(grid[0]):
                return False
            if grid[ i +v][j] == 1 and grid[i][ j +v] == 1 and grid[ i +v][ j +v] == 1:
                for k in range(v):
                    if grid[ i +k][j] != 1 or grid[i][ j +k] != 1 or grid[ i +v][ j +k] != 1 or grid[ i +k][ j +v] != 1:
                        return False
                return True
            return False
        max_len = max(len(grid), len(grid[0]))
        for i in range(len(grid)):
            # print(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] == 1:

                    cur = max_len
                    while cur >= max_val:
                        if check_square(i, j, cur):
                            max_val = cur + 1
                            break
                        cur -= 1
        return max_val * max_val

    
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = [[0] * (n + 1) for _ in range(m + 1)]
        up = [[0] * (n + 1) for _ in range(m + 1)]
        maxBorder = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1]:
                    left[i][j] = left[i][j - 1] + 1
                    up[i][j] = up[i - 1][j] + 1
                    border = min(left[i][j], up[i][j])
                    while left[i - border + 1][j] < border or up[i][j - border + 1] < border:
                        border -= 1
                    maxBorder = max(maxBorder, border)
        return maxBorder ** 2
    
# tips

'''
For each square, know how many ones are up, left, down, and right of this square. You can find it in O(N^2) using dynamic programming.

Now for each square ( O(N^3) ), we can evaluate whether that square is 1-bordered in O(1).
'''
