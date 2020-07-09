'''
面试题 17.13. Re-Space LCCI
Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a lengthy document. A sentence like "I reset the computer. It still didn't boot!" became "iresetthecomputeritstilldidntboot''. You'll deal with the punctuation and capi­talization later; right now you need to re-insert the spaces. Most of the words are in a dictionary but a few are not. Given a dictionary (a list of strings) and the document (a string), design an algorithm to unconcatenate the document in a way that minimizes the number of unrecognized characters. Return the number of unrecognized characters.

Note: This problem is slightly different from the original one in the book.



Example:

Input:
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
Output:  7
Explanation:  After unconcatenating, we got "jess looked just like tim her brother", which containing 7 unrecognized characters.
Note:

0 <= len(sentence) <= 1000
The total number of characters in dictionary is less than or equal to 150000.
There are only lowercase letters in dictionary and sentence.

面试题 17.13. 恢复空格
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数



示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
提示：

0 <= len(sentence) <= 1000
dictionary中总字符数不超过 150000。
你可以认为dictionary和sentence中只包含小写字母。
'''


class Solution(object):

    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """

        if not sentence:
            return 0

        trie = Trie()
        for dict in dictionary:
            trie.insert(dict)

        dp = [0 for i in range(len(sentence))]
        dp[0] = 0 if trie.search(sentence[:1]) else 1
        for i in range(1, len(sentence)):
            dp[i] = dp[i - 1] + 1
            for j in range(i + 1):
                # if sentence[j:i+1] in dictionary:
                if trie.min_len <= i - j + 1 <= trie.max_len and trie.search(sentence[j:i + 1]):
                    if j > 0:
                        dp[i] = min(dp[j - 1], dp[i])
                    else:
                        dp[i] = 0
        # print(dp)
        return dp[-1]


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.min_len = float("inf")
        self.max_len = 0

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
        length = len(word)
        if length > self.max_len:
            self.max_len = length
        if length < self.min_len:
            self.min_len = length
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


# tips

'''
试试递归方法。

你能把所有的可能性都试一试吗？那会是什么样子？

你可以用两种方法中的一种来考虑递归算法：(1)对于每个字符，我应该在这里放一个空格吗？(2)下一个空格应该放在哪里？两种方案都可以递归地解决。

递归算法是否会反复遇到相同的子问题？你能用一个散列表进行优化吗？

在现实生活中，我们知道有些路径不会构成一个词。例如，没有以hellothisism开头的单词。能在明知行不通的情况下提前终止吗？

如果想提前终止，可以试一试trie。
'''