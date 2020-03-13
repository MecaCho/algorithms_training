'''

67. Add Binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


67. 二进制求和
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        i = len_a - 1
        j = len_b - 1
        res = ""
        jin = 0
        while i>=0 or j>=0:
            num_a = 1 if i >= 0 and a[i] == "1" else 0
            num_b = 1 if j >= 0 and b[j] == "1" else 0
            sum_tmp = num_a + num_b + jin
            jin = sum_tmp / 2
            res = str(sum_tmp % 2) + res
            i -= 1
            j -= 1
        res = str(jin) + res if jin >0 else res
        return res


if __name__ == '__main__':
    demo = Solution()
    print(demo.addBinary("1011", "1101"))
