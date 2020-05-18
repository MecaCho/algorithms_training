

'''
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


'''


import re


class Solution1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = "".join([i.lower() for i in re.findall("[A-Za-z0-9]", s)])
        return new_s[::-1] == new_s


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i <= j:
            if re.match('[a-zA-Z0-9]', s[i]) and re.match('[a-zA-Z0-9]', s[j]):
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            elif not re.match('[a-zA-Z0-9]', s[i]):
                i += 1
                continue
            elif not re.match('[a-zA-Z0-9]', s[j]):
                j -= 1
                continue

        return True

    def is_palindrome(self, s):
        s = "".join(filter(lambda x: x.isalnum(), s)).lower()
        return s == s[::-1]