# encoding=utf8

'''
521. Longest Uncommon Subsequence I
Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
 

Example 1:

Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
Example 2:

Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".
Example 3:

Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a.
 

Constraints:

1 <= a.length, b.length <= 100
a and b consist of lower-case English letters.
'''

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return max(len(a), len(b)) if a != b else -1


# tips

'''
若两字符串不相同，那么我们可以选择较长的字符串作为最长特殊序列，
显然它不会是较短的字符串的子序列。特别地，当两字符串长度相同时（但不是同一字符串），
我们仍然可以选择其中的一个字符串作为最长特殊序列，它不会是另一个字符串的子序列。

若两字符串相同，那么任一字符串的子序列均会出现在两个字符串中，此时应返回 −1。
'''
