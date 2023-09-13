# encoding=utf8

'''
2596. Check Knight Tour Configuration

There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.


 

Example 1:


Input: grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
Output: true
Explanation: The above diagram represents the grid. It can be shown that it is a valid configuration.
Example 2:


Input: grid = [[0,3,6],[5,8,1],[2,7,4]]
Output: false
Explanation: The above diagram represents the grid. The 8th move of the knight is not valid considering its position after the 7th move.
 

Constraints:

n == grid.length == grid[i].length
3 <= n <= 7
0 <= grid[row][col] < n * n
All integers in grid are unique.
'''

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(1,2),(2,1),(2, -1),(-2, 1), (1, -2), (-1, 2),(-1, -2), (-2, -1)]
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n
        def valid_step(i, j):
            for x, y in directions:
                if valid(i+x, j+y) and grid[i+x][j+y] == grid[i][j]+1:
                    return [i+x, j+y]
            return []
        i, j = 0, 0
        visted = set()
        visted.add((0, 0))
        while len(visted) != m * n:
            tmp = valid_step(i, j)
            if tmp:
                i,j = tmp[0], tmp[1]
                visted.add((i, j))
            else: 
                return False
        return True


