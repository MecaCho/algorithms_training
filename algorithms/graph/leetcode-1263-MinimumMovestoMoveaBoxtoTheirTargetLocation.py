# encoding=utf8

'''
leetcode-1263-MinimumMovestoMoveaBoxtoTheirTargetLocation.py
1263. Minimum Moves to Move a Box to Their Target Location
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

 

Example 1:


Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation: push the box down, left, left, up and up.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid contains only characters '.', '#', 'S', 'T', or 'B'.
There is only one character 'S', 'B', and 'T' in the grid.
'''


# sample code

from collections import deque
from typing import List


class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((1, 0, -1, 0), (-1, 0, 1, 0), (0, -1, 0, 1), (0, 1, 0, -1))

        def check(start, target, bpos):
            if start == target: return True
            tr, tc = target
            if (not (rows > tr >= 0 <= tc < cols)) or grid[tr][tc] == '#': return False
            q = deque([start])
            vis = {start, bpos}
            while q:
                r, c = q.popleft()
                for dr, dc, _, _ in dirs:
                    nr, nc = r + dr, c + dc
                    if rows > nr >= 0 <= nc < cols and (nr, nc) not in vis and grid[nr][nc] != '#':
                        if (nr, nc) == target:
                            return True
                        vis.add((nr, nc))
                        q.append((nr, nc))
            return False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'S':
                    s = (r, c)
                elif grid[r][c] == 'B':
                    b = (r, c)
                elif grid[r][c] == 'T':
                    t = (r, c)
        if b == t: return 0
        q = deque([(*b, *s, 0)])
        vis = {(*b, *s)}  # ！状态是 箱子位置和方向（人的位置）
        while q:
            r, c, sr, sc, step = q.popleft()
            for dr, dc, dr2, dc2 in dirs:
                nr, nc = r + dr, c + dc  # 箱子目标位置
                nsr, nsc = r + dr2, c + dc2  # 人的目标位置
                if rows > nr >= 0 <= nc < cols and (nr, nc, nsr, nsc) not in vis and grid[nr][nc] != '#' and check((sr, sc), (nsr, nsc), (r, c)):
                    if (nr, nc) == t:
                        return step + 1
                    vis.add((nr, nc, nsr, nsc))
                    q.append((nr, nc, r, c, step + 1))
        return -1


