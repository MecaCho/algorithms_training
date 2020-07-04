'''
44. Wildcard Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false


44. 通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j = 0, 0
        match = 0
        start = -1
        while i < len(s):
            if j < len(p) and (p[j] == "?" or p[j] == s[i]):
                i += 1
                j += 1
                continue
            if j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1
                continue
            if start != -1:
                j = start + 1
                match += 1
                i = match
                continue
            return False

        return all(p[k] == "*" for k in range(j, len(p)))


# Let's briefly summarize the idea of DP. We define the state P[i][j] to be whether s[0..i) matches p[0..j). The
# state equations are as follows:
#
# P[i][j] = P[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '?'), if p[j - 1] != '*';
# P[i][j] = P[i][j - 1] || P[i - 1][j], if p[j - 1] == '*'.

class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp = [[False for _ in range(len(p))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     for j in range(len(p)):
        #         if p[j] == "*":
        #             if i > 0 and j > 0:
        #                 dp[i][j] = dp[i][j-1] or dp[i-1][j]
        #             if j == 0:
        #                 dp[i][j] = True
        #         else:
        #             if i > 0 and j > 0:
        #                 dp[i][j] = dp[i-1][j-1] and (p[j] == "?" or (p[j]==s[i]))
        #             elif j == 0:
        #                 dp[i][0] = p[j] == "?" or (p[j]==s[i]) if i == 0 else False
        #             elif i == 0:
        #                 dp[0][j] = p[j] == "?" or (p[j]==s[i]) if j == 0 else False
        # print(dp)
        # return dp[len(s)-1]


        m, n = len(s), len(p)
        dp = [False for _ in range(m+1)]
        dp[0] = True
        for j in range(1, n+1):
            pre = dp[0]
            dp[0] = dp[0] and p[j-1] == "*"
            for i in range(1, m+1):
                tmp = dp[i]
                if p[j-1] != "*":
                    dp[i] = pre and (s[i-1]==p[j-1] or p[j-1]=="?")
                else:
                    dp[i] = dp[i-1] or dp[i]
                pre = tmp
        return dp[m]
