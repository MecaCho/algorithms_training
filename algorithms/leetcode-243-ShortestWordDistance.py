'''
243. Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

243. 最短单词距离
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。

'''



class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l = -1
        r = -1
        min_seq = float("inf")
        has = False
        for i in range(len(words)):
            if words[i] == word1:
                l = i
            elif words[i] == word2:
                r = i
            if not (l == -1 or r == -1):
                has = True
                min_seq = min(abs(l-r), min_seq)
        if has:
            return min_seq
        else:
            return -1

