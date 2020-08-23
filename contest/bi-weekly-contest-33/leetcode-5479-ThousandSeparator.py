'''
5479. Thousand Separator

Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"


Constraints:

0 <= n < 2^31

5479. 千位分隔数

给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。



示例 1：

输入：n = 987
输出："987"
示例 2：

输入：n = 1234
输出："1.234"
示例 3：

输入：n = 123456789
输出："123.456.789"
示例 4：

输入：n = 0
输出："0"


提示：

0 <= n < 2^31
'''



class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1000:
            return str(n)
        nums = []
        while n:
            nums.append(str(n % 1000).rjust(3, "0"))
            n /= 1000
        return ".".join(nums[::-1]).lstrip("0")


class Solution1(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        return ".".join(findall(r"\d{1,3}",str(n)[::-1]))[::-1]