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


'''
方法一：使用前缀树的回溯
这个问题实际上是一个简化的纵横填字游戏，在这个游戏中，单词的解已经被嵌入了一些无关字母。我们要做的就是把它们划掉。

直观地说，为了划掉所有潜在的单词，总体策略是一个接一个地迭代单元格，然后从每个单元格沿着它的四个潜在方向的走，找到匹配的单词。

当我们在黑板上徘徊时，若我们知道这不会发现新单词时，我们会停止探索。

有人可能已经猜到了我们用来解决这个问题的方法。是的，它是回溯，这将是解决方案的主干。构造一个回溯的解决方案是相当简单的。

解决这个问题的关键在于我们如何从字典中找到单词的匹配项。直观地说，可以使用 hashset 数据结构（例如Python 中的 set()）。

然而，在回溯过程中，人们会更经常地遇到这样的问题：是否存在任何包含特定前缀的单词，而不是是否有一个字符串作为单词存在于字典中。因为如果我们知道给定前缀的字典中不存在任何单词匹配，那么我们就不需要进一步探索某个方向。而这，将大大减少探测空间，从而提高回溯算法的性能。

能够查找前缀的数据结构叫 Trie，于 hashset 比较。Trie 不仅可以检查一个单词，还可以立即找到共享给定前缀的单词。事实证明，数据结构的选择（Trie 与 hashset）可能以排名前 5% 或后 5% 的解决方案结束。

这里我们展示了一个由单词列表构建的 Trie 示例。如下图所示，在所表示的节点处，我们将知道字典中至少有两个前缀为 d 的单词。



我们在实现 Trie 数据结构时遇到麻烦。我们可以从Trie 问题开始作为热身，然后再回来这个问题。

算法：

该算法的整个工作流程是直观的，包括在二维网格中的每个单元上循环和从单元开始的递归函数调用。这是算法的框架。

我们根据字典中的单词构建一个 Trie，稍后将用于匹配过程。
从每个单元格开始，如果字典中存在以单元格中的字母开头的单词,则我们开始回溯探索（即 backtracking(cell)）。
在递归函数 backtracking(cell) 调用过程中，我们探索当前单元格周围的相邻单元格（即 neighborCell）以进行下一个递归调用 backtracking(neighborCell)。在每次调用时，我们都会检查到目前为止遍历的字母序列是否与字典中的任何单词匹配，这需要借助于我们在开始时构建的 Trie 数据结构。
下面是算法的工作原理的。基于上述思想，我们给出了一些示例实现。之后，我们详细介绍了一些可以进一步应用于该算法的优化。



PythonJava
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    
为了更好地理解回溯过程，我们将在下面的动画中演示如何在 Trie 中找到 dog。


1 / 6

优化：

在上述实现中，除了应用 Trie 数据结构外，我们还应用了一些技巧来进一步加快运行时间。特别是，Python 实现的运行速度可以超过 98% 的提交。我们按其重要性将这些技巧详述如下。

沿着 Trie 的节点回溯。
人们可以简单地使用 Trie 作为字典来快速找到单词和前缀的匹配，即在回溯的每一步，我们都从Trie 的根开始。

然而，更有效的方法是将 Trie 与回溯过程一起遍历，即每一步 backtracking(TrieNode)，TrieNode 的深度对应于我们到目前为止匹配的前缀的长度。这项措施可以将您的解决方案从提交的最低 5%5 中脱颖出来。

在回溯过程中逐渐剪除 Trie 中的节点（剪枝）。
这个想法的动机是整个算法的时间复杂度取决于 Trie 的大小。对于 Trie 中的叶节点，一旦遍历它（即找到匹配的单词），就不需要再遍历它了。结果，我们可以把它从树上剪下来。

逐渐地，这些非叶节点可以成为叶节点以后，因为我们修剪他们的孩子叶节点。在极端情况下，一旦我们找到字典中所有单词的匹配项，Trie 就会变成空的。这个剪枝措施可以减少在线测试用例 50% 的运行时间。



从 Trie 中删除匹配的单词。
在这个问题中，我们被要求返回所有匹配的单词，而不是潜在匹配的数量。因此，一旦到达包含单词匹配的特定 Trie 节点，我们就可以从 Trie 中删除匹配单词。

作为附带好处，我们不需要检查结果集中是否有任何重复项。因此，我们可以简单地使用一个列表而不是集合来保存结果，这样可以加快解决方案的速度。

复杂度分析

时间复杂度：\mathcal{O}(M(4\cdot3^{L-1}))O(M(4⋅3 
L−1
 ))，其中MM 是二维网格中的单元格数，LL 是单词的最大长度。
计算回溯算法将执行的确切步数是一个棘手的问题。我们为这个问题的最坏情况提供了该步骤的上限。该算法循环遍历二维网格中的所有单元，因此在复杂度公式中我们有 MM 作为因子。然后将其归结为每个启动单元所需的最大步骤数（即 4\cdot3^{L-1}4⋅3 
L−1
 ）。
假设单词的最大长度是 LL，从一个单元格开始，最初我们最多可以探索 4 个方向。假设每个方向都是有效的（即最坏情况），在接下来的探索中，我们最多有 3 个相邻的单元（不包括我们来的单元）要探索。因此，在回溯探索期间，我们最多遍历 4\cdot3^{L-1}4⋅3 
L−1
  个单元格。
你可能会想最坏的情况是什么样子。这里有一个例子。想象一下，二维网格中的每个单元都包含字母 a，单词词典包含一个单词 ['aaaa']。这是算法将遇到的最坏的情况之一。


注意，上述时间复杂性是在 Trie 数据结构一旦构建就不会改变的假设下估计的。如果采用优化策略逐步删除 Trie 中的节点，则可以大大提高时间复杂度，因为一旦匹配词典中的所有单词，即 Trie 变为空，回溯的成本就会降低到零。

空间复杂度：\mathcal{O}(N)O(N)，其中 NN 是字典中的字母总数。
算法消耗的主要空间是我们构建的 Trie 数据结构。在最坏的情况下，如果单词之间没有前缀重叠，则 Trie 将拥有与所有单词的字母一样多的节点。也可以选择在 Trie 中保留单词的副本。因此，我们可能需要 2N2N 的空间用于 Trie。

作者：LeetCode
链接：https://leetcode-cn.com/problems/word-search-ii/solution/dan-ci-sou-suo-ii-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''