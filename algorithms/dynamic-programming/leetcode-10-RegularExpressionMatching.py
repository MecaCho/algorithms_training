
'''
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #         解题思路
        # 1、如果p为空，s为空匹配，s非空不匹配；
        # 2、s非空，p == s || p == '.'时第一个字符匹配；
        # 3、(p+1) != ''，则递归判断剩下的是否匹配 first_match && isMatch(++s, ++p)
        # 4、(p+1) == '*'，则有两种情况匹配：
        # a: *匹配0个字符，s匹配剩下的，即isMatch(s, p+2)
        # b: *匹配1个字符，继续用p匹配剩下的s，即first_match && isMatch(s+1, p)

        # 代码
        # bool isMatch(char * s, char * p){
        #     if (!*p) return !*s;
        #     bool first_match = *s && (*s == *p || *p == '.');
        #     if (*(p+1) == '*') {
        #         return isMatch(s, p+2) || (first_match && isMatch(++s, p));
        #     }
        #     else {
        #         return first_match && isMatch(++s, ++p);
        #     }
        # }
        #         first_match = bool(text) and pattern[0] in {text[0], '.'}

        # if len(pattern) >= 2 and pattern[1] == '*':
        #     return (self.isMatch(text, pattern[2:]) or
        #             first_match and self.isMatch(text[1:], pattern))
        # else:
        #     return first_match and self.isMatch(text[1:], pattern[1:])
        # print(s, p)
        if not p:
            print(not s, s)
            return not s
        first_match = True if s and (s[0] == p[0] or p[0] == ".") else False

        # print(first_match)

        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        # 如果 p.charAt(j) == s.charAt(i) : dp[i][j] = dp[i-1][j-1]；
        # 如果 p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1]；
        # 如果 p.charAt(j) == '*'：
        # 如果 p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2] //in this case, a* only counts as empty
        # 如果 p.charAt(j-1) == s.charAt(i) or p.charAt(i-1) == '.'：
        # dp[i][j] = dp[i-1][j] //in this case, a* counts as multiple a
        # or dp[i][j] = dp[i][j-1] // in this case, a* counts as single a
        # or dp[i][j] = dp[i][j-2] // in this case, a* counts as empty

        # s_len = len(s)
        # p_len = len(p)
        # dp = [[False for _ in range(p_len)] for _ in range(s_len)]
        # # for i in range(s_len):
        # dp[0][0] = True
        # for i in range(s_len):
        #     for j in range(p_len):
        #         if i >= 0 and p[j] == s[i] or p[j] == ".":
        #             print(i, j, dp[i-1][j-1])
        #             dp[i][j] = dp[i-1][j-1] if i > 0 and j > 0 else True
        #         elif p[j] == "*":
        #             if p[j-1] != s[i]:
        #                 dp[i][j] = dp[i][j-2]
        #             elif p[j-1] == s[i] or p[j-1] == ".":
        #                 dp[i][j] = (dp[i-1][j] or dp[i][j-1] or dp[i][j-2])

        # print(dp)
        # return dp[-1][-1]
