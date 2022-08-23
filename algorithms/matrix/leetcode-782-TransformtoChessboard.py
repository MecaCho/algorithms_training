# encoding=utf8

'''
782. Transform to Chessboard
You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.

Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.

A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

 

Example 1:


Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.
Example 2:


Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
Example 3:


Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
 

Constraints:

n == board.length
n == board[i].length
2 <= n <= 30
board[i][j] is either 0 or 1.
'''

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if n <= 1:
            return 0
        rows=[''.join(str(c) for c in r) for r in board]
        counter = collections.Counter(rows)
        keys = list(counter)
        if len(keys) != 2 or abs(counter[keys[0]]-counter[keys[1]]) > 1 \
            or abs(keys[0].count('1')-keys[0].count('0')) > 1 \
            or any(a==b for a,b in zip(*keys)):
            return -1
        rowdiff = sum(board[0][i] != (i%2) for i in range(n))
        coldiff = sum(board[i][0] != (i%2) for i in range(n))
        rowdiff = n - rowdiff if rowdiff%2 != 0 or (n%2==0 and (n-rowdiff)<rowdiff) else rowdiff
        coldiff = n - coldiff if coldiff%2 != 0 or (n%2==0 and (n-coldiff)<coldiff) else coldiff
        return (rowdiff+coldiff) // 2
   
