# encoding=utf8


'''

244. Shortest Word Distance II
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


244. 最短单词距离 II
请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
'''


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict
        self.word_dict = defaultdict(list)
        for i in range(len(words)):
            self.word_dict[words[i]].append(i)
        self.words = words


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l_list = self.word_dict[word1]
        r_list = self.word_dict[word2]
        min_seq = float("inf")
        if not l_list or not r_list:
            return -1
        i = j = 0
        while i < len(l_list) and j < len(r_list):
            left = l_list[i]
            right = r_list[j]
            min_seq = min(min_seq, abs(right - left))
            if left < right:
                i += 1
            else:
                j += 1
        return min_seq



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)