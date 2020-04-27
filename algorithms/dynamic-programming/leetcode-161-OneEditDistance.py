'''

161. 相隔为 1 的编辑距离
给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

注意：

满足编辑距离等于 1 有三种可能的情形：

往 s 中插入一个字符得到 t
从 s 中删除一个字符得到 t
在 s 中替换一个字符得到 t
示例 1：

输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。
示例 2:

输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。
示例 3:

输入: s = "1203", t = "1213"
输出: true
解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。

161. One Edit Distance
Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
'''


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            s, t = t, s
        if len(t) - len(s) > 1:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) < len(t):
                    return s[i:] == t[ i +1:]
                else:
                    return s[ i +1:] == t[ i +1:]

        return len(t) - len(s) == 1
