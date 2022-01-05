# encoding=utf8

'''
1576. Replace All ?'s to Avoid Consecutive Repeating Characters
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.



Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"


Constraints:

1 <= s.length <= 100

s contains only lower case English letters and '?'.


1576. 替换所有的问号
给你一个仅包含小写英文字母和 '?' 字符的字符串 s<var> </var>，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。

注意：你 不能 修改非 '?' 字符。

题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。



示例 1：

输入：s = "?zs"
输出："azs"
解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两个 'z' 。
示例 2：

输入：s = "ubv?w"
输出："ubvaw"
解释：该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。
示例 3：

输入：s = "j?qg??b"
输出："jaqgacb"
示例 4：

输入：s = "??yw?ipkj?"
输出："acywaipkja"


提示：

1 <= s.length <= 100

s 仅包含小写英文字母和 '?' 字符
'''




class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        length = len(s)

        s_list = list(s)

        count = 0
        while i < length:
            if s[i] == "?":
                if i > 0 and s[i-1] == "a":
                    count = 1
                if count >= 26:
                    count = 0
                replace_chr = chr(ord("a") + count)
                s_list[i] = replace_chr if i < length-1 and s[i+1] != replace_chr  else chr(ord("a") + count+1)
                count += 1
            else:
                count = 0
            i += 1
        # print(s_list)
        return "".join(s_list)

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        for i in range(len(l)):
            if l[i] == "?":
                l[i] = "a"
                while (i+1 < len(l) and l[i] == l[i+1]) or (l[i-1] == l[i] and i-1 >= 0):
                    l[i] = chr(ord(l[i]) + 1)
        return "".join(l)
