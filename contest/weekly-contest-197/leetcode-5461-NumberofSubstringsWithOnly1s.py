'''
5461. Number of Substrings With Only 1s
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0


Constraints:

s[i] == '0' or s[i] == '1'
1 <= s.length <= 10^5


5461. 仅含 1 的子串数
给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。

返回所有字符都为 1 的子字符串的数目。

由于答案可能很大，请你将它对 10^9 + 7 取模后返回。



示例 1：

输入：s = "0110111"
输出：9
解释：共有 9 个子字符串仅由 '1' 组成
"1" -> 5 次
"11" -> 3 次
"111" -> 1 次
示例 2：

输入：s = "101"
输出：2
解释：子字符串 "1" 在 s 中共出现 2 次
示例 3：

输入：s = "111111"
输出：21
解释：每个子字符串都仅由 '1' 组成
示例 4：

输入：s = "000"
输出：0


提示：

s[i] == '0' 或 s[i] == '1'
1 <= s.length <= 10^5
'''



class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        # def get_num(n):
        #     return n * (n+1) / 2
        one_list = [i for i in re.split("0*", s) if i]

        res = 0
        # print(one_list)
        for l in one_list:
            num = len(l)
            res += num * (num+1)/2
            res %= 10**9 + 7
        return res

# tips

'''
Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.
'''
