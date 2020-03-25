'''
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''
class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s ) -1
        count = 1
        def is_palindrome(s):
            # s = "".join(filter(lambda x: x.isalnum(), s)).lower()
            return s == s[::-1]
        while i <= j:
            if s[i] != s[j]:
                return is_palindrome(s[i:j]) or is_palindrome(s[ i +1: j +1])
            else:
                i += 1
                j -= 1

        return True
