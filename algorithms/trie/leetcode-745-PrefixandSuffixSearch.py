'''
745. 前缀和后缀搜索
给定多个 words，words[i] 的权重为 i 。

设计一个类 WordFilter 实现函数WordFilter.f(String prefix, String suffix)。这个函数将返回具有前缀 prefix 和后缀suffix 的词的最大权重。如果没有这样的词，返回 -1。

例子:

输入:
WordFilter(["apple"])
WordFilter.f("a", "e") // 返回 0
WordFilter.f("b", "") // 返回 -1
注意:

words的长度在[1, 15000]之间。
对于每个测试用例，最多会有words.length次对WordFilter.f的调用。
words[i]的长度在[1, 10]之间。
prefix, suffix的长度在[0, 10]之前。
words[i]和prefix, suffix只包含小写字母。


745. Prefix and Suffix Search
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1


Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
'''


import collections

Trie = lambda: collections.defaultdict(Trie)

# class Trie(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = {}

#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         tree = self.root
#         for w in word:
#             if tree is None or not tree.get(w):
#                 tree[w] = {}
#             tree = tree.get(w)
#         tree["end"] = True

#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         tree = self.root
#         for w in word:
#             tree = tree.get(w)
#             if tree is None:
#                 print(tree)
#                 tree = tree.items()
#                 # return False
#         return True if tree.get("end") else False


#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         tree = self.root
#         for w in prefix:
#             tree = tree.get(w)
#             if tree is None:
#                 return False
#         return True

class WordFilter(object):
    def __init__(self, words):

        # self.trie = collections.defaultdict(Trie)
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in xrange(len(word)):
                cur = self.trie
                cur[False] = weight
                for j in xrange(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[False] = weight
        # print(self.trie)

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[False]



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


# tips

'''
For a word like "test", consider "#test", "t#test", "st#test", "est#test", "test#test". Then if we have a query like prefix = "te", suffix = "t", we can find it by searching for something we've inserted starting with "t#te".
'''