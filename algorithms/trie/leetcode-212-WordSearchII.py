'''
212. 单词搜索 II
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

212. Word Search II
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tree = self.root
        for w in word:
            if tree is None or not tree.get(w):
                tree[w] = {}
            tree = tree.get(w)
        tree["end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.root
        for w in word:
            tree = tree.get(w)
            if tree is None:
                return False
        return True if tree.get("end") else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.root
        for w in prefix:
            tree = tree.get(w)
            if tree is None:
                return False
        return True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        add_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        col_len = len(board)
        if not col_len or not words or not board[0]:
            return []
        row_len = len(board[0])

        trie = Trie()

        max_length = 0
        for word in words:
            trie.insert(word)
            if len(word) > max_length:
                max_length = len(word)

        self.w = []

        def dfs(res, i, j):
            if i < 0 or j < 0 or i >= col_len or j >= row_len or board[i][j] == "":
                if trie.search(res) and res not in self.res:
                    self.res.append(res)
            else:
                tmp = board[i][j]
                board[i][j] = ""
                for add_i, add_j in add_list:
                    if len(res) < max_length and trie.startsWith(res + str(tmp)):
                        dfs(res + str(tmp), i + add_i, j + add_j)
                board[i][j] = tmp

        self.res = []

        for i in range(col_len):
            for j in range(row_len):
                if board[i][j] in trie.root:
                    # print(board[i][j], trie.root)
                    dfs("", i, j)

        return sorted(self.res)
