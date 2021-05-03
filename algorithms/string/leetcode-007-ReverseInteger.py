'''

7. Reverse Integer
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


7. 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        res = int(str(x)[::-1].lstrip("0") if x > 0 else "-" + str(x)[:0:-1].lstrip("0"))
        if -2**31<res<2**31-1:
            return res
        return 0
       
       
       
class Solution20210503(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = False
        if x < 0:
            x = -x
            flag = True
        res = 0
        while x:
            num = x % 10
            res = 10 * res + num
            x /= 10
        if -2**31 <= res <= 2**31-1:
            return -res if flag else res
        return 0

       
