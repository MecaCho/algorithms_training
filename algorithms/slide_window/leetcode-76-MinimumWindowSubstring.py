
'''
76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''







class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map = collections.Counter(t)
        res = ''
        n = 0
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch not in t_map:
                continue
            t_map[ch] -= 1
            if t_map[ch] == 0:
                n += 1
            while s[l] not in t_map or t_map[s[l]] < 0:
                if s[l] in t_map:
                    t_map[s[l]] += 1
                l += 1
            if n == len(t_map):
                if not res or len(res) > r - l + 1:
                    res = s[l: r+1]
        return res

