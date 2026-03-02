# encoding=utf8

'''
1536. Minimum Swaps to Arrange a Binary Grid

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:

Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3

Example 2:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0

 

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 200
    grid[i][j] is either 0 or 1
'''

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Helper to count trailing zeros in a row
        def count_trailing_zeros(row):
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            return count
        
        # Calculate trailing zeros for each row
        zeros = [count_trailing_zeros(row) for row in grid]
        
        swaps = 0
        
        # Iterate through each row position i from 0 to n-1
        for i in range(n):
            # The number of trailing zeros required for row i
            required = n - 1 - i
            
            # Find the first row k (starting from i) that satisfies the requirement
            k = i
            while k < n and zeros[k] < required:
                k += 1
            
            # If no such row is found, it's impossible
            if k == n:
                return -1
            
            # If the row is not already in position i, swap it up
            if k != i:
                # Add the number of adjacent swaps needed (distance)
                swaps += (k - i)
                
                # Simulate the swaps: Move zeros[k] to position i
                # Shift elements from i to k-1 down by one
                val = zeros.pop(k)
                zeros.insert(i, val)
                
        return swaps

