
'''
266. 回文排列
给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

示例 1：

输入: "code"
输出: false
示例 2：

输入: "aab"
输出: true
示例 3：

输入: "carerac"
输出: true

266. Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''




class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(s)):
            c = s[i]
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        count = 0
        for k, v in hash_map.items():
            if v % 2 != 0:
                count += 1
        return count < 2
