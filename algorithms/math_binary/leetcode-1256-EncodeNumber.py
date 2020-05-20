


'''
1256. 加密数字
给你一个非负整数 num ，返回它的「加密字符串」。

加密的过程是把一个整数用某个未知函数进行转化，你需要从下表推测出该转化函数：





示例 1：

输入：num = 23
输出："1000"
示例 2：

输入：num = 107
输出："101100"


提示：

0 <= num <= 10^9

1256. Encode Number
Given a non-negative integer num, Return its encoding string.

The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:





Example 1:

Input: num = 23
Output: "1000"
Example 2:

Input: num = 107
Output: "101100"


Constraints:

0 <= num <= 10^9
'''


class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        return bin(num+1)[3:]
