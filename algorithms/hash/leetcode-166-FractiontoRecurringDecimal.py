# encoding=utf8

'''
166. Fraction to Recurring Decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.



Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"


Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0

166. 分数到小数
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。



示例 1：

输入：numerator = 1, denominator = 2
输出："0.5"
示例 2：

输入：numerator = 2, denominator = 1
输出："2"
示例 3：

输入：numerator = 2, denominator = 3
输出："0.(6)"
示例 4：

输入：numerator = 4, denominator = 333
输出："0.(012)"
示例 5：

输入：numerator = 1, denominator = 5
输出："0.2"


提示：

-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''



class Solution1:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):  # 正负号判断，异或
            res.append("-")

        numer = abs(numerator)  # 取整
        denomin = abs(denominator)

        a, remaind = divmod(numer, denomin)
        res.append(str(a))
        if remaind == 0:  # 整除，直接返回
            return "".join(res)

        res.append(".")  # 添加小数点
        dic = {}
        while remaind != 0:
            if remaind in dic:  # 如果有循环，添加括号
                res.insert(dic[remaind], "(")
                res.append(")")
                break

            dic[remaind] = len(res)  # 记录括号的位置
            remaind *= 10  # 余数加0，继续除法
            a, remaind = divmod(remaind, denomin)
            res.append(str(a))

        return "".join(res)



class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        is_neg = True if numerator * denominator < 0 else False

        a, b = abs(numerator), abs(denominator)
        lt_zero = True if a < b else False
        res = []
        if not lt_zero:
            res.append(a/b)
            a = a % b
            if a != 0:
                res.append(".")

        num_map = {}
        while a != 0:
            if a in num_map:
                print res, num_map
                res.insert(num_map[a], "(")
                res.append(")")
                break
            tmp = a

            count = 0
            while a < b:
                a *= 10
                count += 1
                if not res or count > 1:
                    res.append(0)

            num, a = divmod(a, b)
            num_map[tmp] = len(res)
            print num, a
            res.append(num)

        if res[0] == 0:
            res[0] = "0."
        res = "".join([str(i) for i in res])
        if is_neg:
            return "-" + res
        return res


if __name__ == '__main__':
    demo = Solution()
    res = demo.fractionToDecimal(-1, 300)
    print res
