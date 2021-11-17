# encoding=utf8

'''
318. Maximum Product of Word Lengths
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
 

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hash = [0]*len(words)
        for i in range(len(words)):
            for ch in words[i]:
                hash[i] |= 1 << (ord(ch) - ord("a"))
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if hash[i] & hash[j] == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res

