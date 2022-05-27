# encoding=utf8

'''
面试题 17.11. Find Closest LCCI
You have a large text file containing words. Given any two different words, find the shortest distance (in terms of number of words) between them in the file. If the operation will be repeated many times for the same file (but different pairs of words), can you optimize your solution?

Example:

Input: words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
Output: 1
Note:

words.length <= 100000

'''

class Solution(object):
    def findClosest(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1, index2 = -1, -1
        res  = 100001
        for i, w in enumerate(words):
            if w == word1:
                index1 = i
            elif w == word2:
                index2 = i

            if index1 != -1 and index2 != -1:
                res = min(res, abs(index1-index2))

        return res


