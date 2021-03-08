# encoding=utf8

'''
132. Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1


Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.


132. 分割回文串 II
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。



示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1


提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成
'''


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # self.vals = []

        # def bk(nums, temp):
        #     if not nums and temp[-1][::-1] == temp[-1]:
        #         self.vals.append(temp)
        #         return
        #     for i in range(len(nums)):
        #         if temp and temp[-1][::-1] != temp[-1]:
        #             continue
        #         bk(nums[ i +1:], temp +["".join(nums[: i +1])])

        # bk(list(s), [])
        # return len(min(self.vals, key=lambda x: len(x))) - 1

        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)

        return f[n - 1]




