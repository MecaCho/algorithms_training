
'''
1271. 十六进制魔术数字
你有一个十进制数字，请按照此规则将它变成「十六进制魔术数字」：首先将它变成字母大写的十六进制字符串，然后将所有的数字 0 变成字母 O ，将数字 1  变成字母 I 。

如果一个数字在转换后只包含 {"A", "B", "C", "D", "E", "F", "I", "O"} ，那么我们就认为这个转换是有效的。

给你一个字符串 num ，它表示一个十进制数 N，如果它的十六进制魔术数字转换是有效的，请返回转换后的结果，否则返回 "ERROR" 。



示例 1：

输入：num = "257"
输出："IOI"
解释：257 的十六进制表示是 101 。
示例 2：

输入：num = "3"
输出："ERROR"


提示：

1 <= N <= 10^12
给定字符串不会有前导 0 。
结果中的所有字母都应该是大写字母。

1271. Hexspeak
A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".



Example 1:

Input: num = "257"
Output: "IOI"
Explanation:  257 is 101 in hexadecimal.
Example 2:

Input: num = "3"
Output: "ERROR"


Constraints:

1 <= N <= 10^12
There are no leading zeros in the given string.
All answers must be in uppercase letters.
'''





class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        num = int(num)
        hash_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 0: "O", 1: "I"}
        res = ""
        while num:
            val = num % 16
            if val <= 9 and val not in [0, 1]:
                return "ERROR"
            res = hash_map[val] + res
            num /= 16
        return res
