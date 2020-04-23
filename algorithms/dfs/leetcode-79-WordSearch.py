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
