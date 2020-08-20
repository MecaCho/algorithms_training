'''
529. Minesweeper
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:



Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

529. 扫雷游戏
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。


示例 1：

输入:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:

示例 2：

输入:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:



注意：

输入矩阵的宽和高的范围为 [1,50]。
点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
输入面板不会是游戏结束的状态（即有地雷已被挖出）。
简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。

'''


class Solution(object):

    DIRECITONS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        m, n = len(board), len(board[0])
        check = lambda i, j, char: 0 <= i < m and 0 <= j < n and board[i][j] == char

        def count_miners(i, j):
            miners = 0
            for ni, nj in self.DIRECITONS:
                ni, nj = ni + i, nj + j
                miners += check(ni, nj, 'M')

            return miners

        def dfs(i, j):
            miners = count_miners(i, j)
            if not miners:
                board[i][j] = 'B'
                for ni, nj in self.DIRECITONS:
                    ni, nj = ni + i, nj + j
                    if check(ni, nj, 'E'):
                        dfs(ni, nj)
            else:
                board[i][j] = str(miners)

        dfs(*click)

        return board


# solution

'''
方法一：深度优先搜索 + 模拟
思路与算法

由于题目要求你根据规则来展示执行一次点击操作后游戏面板的变化，所以我们只要明确该扫雷游戏的规则，并用代码模拟出来即可。

那我们着眼于题目的规则，会发现总共分两种情况：

当前点击的是「未挖出的地雷」，我们将其值改为 \text{X}X 即可。
当前点击的是「未挖出的空方块」，我们需要统计它周围相邻的方块里地雷的数量 \textit{cnt}cnt（即 \text{M}M 的数量）。如果 \textit{cnt}cnt 为零，即执行规则 22，此时需要将其改为 \text{B}B，且递归地处理周围的八个未挖出的方块，递归终止条件即为规则 44，没有更多方块可被揭露的时候。否则执行规则 33，将其修改为数字即可。
整体看来，一次点击过程会从一个位置出发，逐渐向外圈扩散，所以这引导我们利用「搜索」的方式来实现。这里以深度优先搜索为例：我们定义递归函数 dfs(x, y) 表示当前在 (x,y)(x,y) 点，执行扫雷规则的情况，我们只要按照上面理出来的情况来进行模拟即可，在 \textit{cnt}cnt 为零的时候，对当前点相邻的未挖出的方块调用递归函数，否则将其改为数字，结束递归。

代码

C++JavaCGolang

var dirX = []int{0, 1, 0, -1, 1, 1, -1, -1}
var dirY = []int{1, 0, -1, 0, 1, -1, 1, -1}

func updateBoard(board [][]byte, click []int) [][]byte {
    x, y := click[0], click[1]
    if board[x][y] == 'M' {
        board[x][y] = 'X'
    } else {
        dfs(board, x, y)
    }
    return board
}

func dfs(board [][]byte, x, y int) {
    cnt := 0
    for i := 0; i < 8; i++ {
        tx, ty := x + dirX[i], y + dirY[i]
        if tx < 0 || tx >= len(board) || ty < 0 || ty >= len(board[0]) {
            continue
        }
        // 不用判断 M，因为如果有 M 的话游戏已经结束了
        if board[tx][ty] == 'M' {
            cnt++
        }
    }
    if cnt > 0 {
        board[x][y] = byte(cnt + '0')
    } else {
        board[x][y] = 'B'
        for i := 0; i < 8; i++ {
            tx, ty := x + dirX[i], y + dirY[i]
            // 这里不需要在存在 B 的时候继续扩展，因为 B 之前被点击的时候已经被扩展过了
            if tx < 0 || tx >= len(board) || ty < 0 || ty >= len(board[0]) || board[tx][ty] != 'E' {
                continue
            }
            dfs(board, tx, ty)
        }
    }
}
复杂度分析

时间复杂度：O(nm)O(nm)，其中 nn 和 mm 分别代表面板的宽和高。最坏情况下会遍历整个面板。
空间复杂度：O(nm)O(nm)。空间复杂度取决于递归的栈深度，而递归栈深度在最坏情况下有可能遍历整个面板而达到 O(nm)O(nm)。
方法二：广度优先搜索 + 模拟
思路与算法

同样地，我们也可以将深度优先搜索改为广度优先搜索来模拟，我们只要在\textit{cnt}cnt 为零的时候，将当前点相邻的未挖出的方块加入广度优先搜索的队列里即可，其他情况不加入队列，这里不再赘述。

代码

C++JavaCGolang

var dirX = []int{0, 1, 0, -1, 1, 1, -1, -1}
var dirY = []int{1, 0, -1, 0, 1, -1, 1, -1}

func updateBoard(board [][]byte, click []int) [][]byte {
    x, y := click[0], click[1]
    if board[x][y] == 'M' {
        board[x][y] = 'X'
    } else {
        bfs(board, x, y)
    }
    return board
}

func bfs(board [][]byte, sx, sy int) {
    queue := [][]int{}
    vis := make([][]bool, len(board))
    for i := 0; i < len(vis); i++ {
        vis[i] = make([]bool, len(board[0]))
    }
    queue = append(queue, []int{sx, sy})
    vis[sx][sy] = true
    for i := 0; i < len(queue); i++ {
        cnt, x, y := 0, queue[i][0], queue[i][1]
        for i := 0; i < 8; i++ {
        tx, ty := x + dirX[i], y + dirY[i]
            if tx < 0 || tx >= len(board) || ty < 0 || ty >= len(board[0]) {
                continue
            }
            // 不用判断 M，因为如果有 M 的话游戏已经结束了
            if board[tx][ty] == 'M' {
                cnt++
            }
        }
        if cnt > 0 {
            board[x][y] = byte(cnt + '0')
        } else {
            board[x][y] = 'B'
            for i := 0; i < 8; i++ {
                tx, ty := x + dirX[i], y + dirY[i]
                // 这里不需要在存在 B 的时候继续扩展，因为 B 之前被点击的时候已经被扩展过了
                if tx < 0 || tx >= len(board) || ty < 0 || ty >= len(board[0]) || board[tx][ty] != 'E' || vis[tx][ty] {
                    continue
                }
                queue = append(queue, []int{tx, ty})
                vis[tx][ty] = true
            }
        }
    }
}
复杂度分析

时间复杂度：O(nm)O(nm)，其中 nn 和 mm 分别代表面板的宽和高。最坏情况下会遍历整个面板。
空间复杂度：O(nm)O(nm)。我们需要 O(nm)O(nm) 的标记数组来标记当前位置是否已经被加入队列防止重复计算。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/minesweeper/solution/sao-lei-you-xi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''