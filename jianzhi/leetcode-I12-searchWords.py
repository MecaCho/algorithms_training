'''
面试题12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。



示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        add_list = [(1 ,0), (-1 ,0), (0 ,1), (0, -1)]
        col_len = len(board)
        if not col_len or not word or not board[0]:
            return False
        row_len = len(board[0])
        self.val_list = []
        marks = [[False for j in range(row_len)] for i in range(col_len)]

        def dfs(i, j, k):

            if i < 0 or j < 0 or i >= col_len or j >= row_len:
                return False
            if not board[i][j] or board[i][j] != word[k]:
                return False
            if k+ 1 >= len(word):
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
                    # print(word[0], self.val_list)
                    # word in self.val_list

        return False

