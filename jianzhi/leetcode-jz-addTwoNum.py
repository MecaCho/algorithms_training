
'''
面试题65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。



示例:

输入: a = 1, b = 1
输出: 2


提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数
'''



class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a &= 0xffffffff
        b &= 0xffffffff
        sum_, carry = 0, 0
        while b != 0:
            # 异或操作得无进位和
            sum_ = a ^ b

            # 与操作后移位得进位值
            carry = ((a & b) << 1) & 0xffffffff

            # 循环，直到进位为0
            a = sum_
            b = carry


        return a if a < 0x80000000 else ~(a^0xffffffff)



class Solution1:
    def add(self, a: int, b: int) -> int:
        a &= 0xffffffff
        b &= 0xffffffff
        while b != 0:
            carry = ((a & b) << 1) & 0xffffffff
            a ^= b
            b = carry
        return a if a < 0x80000000 else ~(a^0xffffffff)
