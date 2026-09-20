# encoding=utf8


'''
3498. Reverse Degree of a String
Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:

1. For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
2. Sum these products for all characters in the string.

Return the reverse degree of s.

 

Example 1:

Input: s = "abc"
Output: 148
Explanation:
Letter  Index in Reversed Alphabet  Index in String  Product
'a'     26                          1                26
'b'     25                          2                50
'c'     24                          3                72

The reversed degree is 26 + 50 + 72 = 148.

Example 2:

Input: s = "zaza"
Output: 160
Explanation:
Letter  Index in Reversed Alphabet  Index in String  Product
'z'     1                           1                1
'a'     26                          2                52
'z'     1                           3                3
'a'     26                          4                104

The reverse degree is 1 + 52 + 3 + 104 = 160.

 

Constraints:

1 <= s.length <= 1000
s contains only lowercase English letters.


3498. 字符串的反转度
给你一个字符串 s，计算其 反转度。

反转度的计算方法如下：

1. 对于每个字符，将其在 反转 字母表中的位置（'a' = 26, 'b' = 25, ..., 'z' = 1）与其在字符串中的位置（下标从 1 开始）相乘。
2. 将这些乘积加起来，得到字符串中所有字符的和。

返回 反转度。

 

示例 1：

输入：s = "abc"
输出：148
解释：
字母  反转字母表中的位置  字符串中的位置  乘积
'a'   26                  1               26
'b'   25                  2               50
'c'   24                  3               72

反转度是 26 + 50 + 72 = 148 。

示例 2：

输入：s = "zaza"
输出：160
解释：
字母  反转字母表中的位置  字符串中的位置  乘积
'z'   1                   1               1
'a'   26                  2               52
'z'   1                   3               3
'a'   26                  4               104

反转度是 1 + 52 + 3 + 104 = 160 。

 

提示：

1 <= s.length <= 1000
s 仅包含小写字母。
'''


class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s, 1):
            weight = 26 - (ord(c) - ord('a'))
            ans += i * weight
        return ans


# golang solution

'''
func reverseDegree(s string) int {
	ans := 0
	for i, c := range s {
		weight := 26 - int(c-'a')
		ans += (i + 1) * weight
	}
	return ans
}
'''
