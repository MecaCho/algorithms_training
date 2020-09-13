'''
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false


提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

79. Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        add_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        col_len = len(board)
        if not col_len or not word or not board[0]:
            return False
        row_len = len(board[0])

        def dfs(i, j, k):
            if i < 0 or j < 0 or i >= col_len or j >= row_len:
                return False
            if not board[i][j] or board[i][j] != word[k]:
                return False
            if k + 1 >= len(word):
                return True
            tmp = board[i][j]
            board[i][j] = ""
            for add_i, add_j in add_list:
                res = dfs(i + add_i, j + add_j, k + 1)
                if res:
                    return True
            board[i][j] = tmp

        for i in range(col_len):
            for j in range(row_len):
                if word[0] == board[i][j]:
                    res = dfs(i, j, 0)
                    if res:
                        return True

        return False


class Solution20200913(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        add_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.res = False
        col, row = len(board[0]), len(board)

        def dfs(i, j, length):
            if length == len(word):
                return True

            if i < 0 or j < 0 or i >= row or j >= col or word[length] != board[i][j] or not board[i][j]:
                return False
            tmp = board[i][j]
            board[i][j] = ""
            for x, y in add_list:
                res = dfs(i + x, j + y, length + 1)
                if res:
                    return True
            board[i][j] = tmp

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    res = dfs(i, j, 0)
                    if res:
                        return res
        return False


# solutions

'''
方法一：深度优先搜索
思路与算法

设函数 \text{check}(i, j, k)check(i,j,k) 判断以网格的 (i, j)(i,j) 位置出发，能否搜索到单词 \text{word}[k..]word[k..]，其中 \text{word}[k..]word[k..] 表示字符串 \text{word}word 从第 kk 个字符开始的后缀子串。如果能搜索到，则返回 \text{true}true，反之返回 \text{false}false。函数 \text{check}(i, j, k)check(i,j,k) 的执行步骤如下：

如果 \text{board}[i][j] \neq s[k]board[i][j] 

​	
 =s[k]，当前字符不匹配，直接返回 \text{false}false。
如果当前已经访问到字符串的末尾，且对应字符依然匹配，此时直接返回 \text{true}true。
否则，遍历当前位置的所有相邻位置。如果从某个相邻位置出发，能够搜索到子串 \text{word}[k+1..]word[k+1..]，则返回 \text{true}true，否则返回 \text{false}false。
这样，我们对每一个位置 (i,j)(i,j) 都调用函数 \text{check}(i, j, 0)check(i,j,0) 进行检查：只要有一处返回 \text{true}true，就说明网格中能够找到相应的单词，否则说明不能找到。

为了防止重复遍历相同的位置，需要额外维护一个与 \text{board}board 等大的 \text{visited}visited 数组，用于标识每个位置是否被访问过。每次遍历相邻位置时，需要跳过已经被访问的位置。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False
复杂度分析

时间复杂度：一个非常宽松的上界为 O(MN \cdot 3^L)O(MN⋅3 
L
 )，其中 M, NM,N 为网格的长度与宽度，LL 为字符串 \text{word}word 的长度。在每次调用函数 \text{check}check 时，除了第一次可以进入 44 个分支以外，其余时间我们最多会进入 33 个分支（因为每个位置只能使用一次，所以走过来的分支没法走回去）。由于单词长为 LL，故 \text{check(i, j, 0)}check(i, j, 0) 的时间复杂度为 O(3^L)O(3 
L
 )，而我们要执行 O(MN)O(MN) 次检查。然而，由于剪枝的存在，我们在遇到不匹配或已访问的字符时会提前退出，终止递归流程。因此，实际的时间复杂度会远远小于 \Theta(MN \cdot 3^L)Θ(MN⋅3 
L
 )。

空间复杂度：O(MN)O(MN)。我们额外开辟了 O(MN)O(MN) 的 \text{visited}visited 数组，同时栈的深度最大为 O(\min(L, MN))O(min(L,MN))。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''