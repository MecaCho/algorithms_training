'''
1180. Count Substrings with Only One Distinct Letter
Given a string S, return the number of substrings that have only one distinct letter.

 

Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: S = "aaaaaaaaaa"
Output: 55
 

Constraints:

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.

1180. 统计只含单一字母的子串
给你一个字符串 S，返回只含 单一字母 的子串个数。

示例 1：

输入： "aaaba"
输出： 8
解释： 
只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
"aaa" 出现 1 次。
"aa" 出现 2 次。
"a" 出现 4 次。
"b" 出现 1 次。
所以答案是 1 + 2 + 4 + 1 = 8。
示例 2:

输入： "aaaaaaaaaa"
输出： 55
 

提示：

1 <= S.length <= 1000
S[i] 仅由小写英文字母组成。
'''


class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        sg = []
        for i in range(len(S)):
            if not sg or S[i] != sg[-1][0]:
                sg.append(S[i])
            else:
                sg[-1] += S[i]
        res = 0
        for s in sg:
            res += (len(s) * (len(s) + 1) /2)
        return res if S else 1
