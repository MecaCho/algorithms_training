'''
面试题 16.01. Swap Numbers LCCI
Write a function to swap a number in place (that is, without temporary vari­ ables).

Example:

Input: numbers = [1,2]
Output: [2,1]
Note:

numbers.length == 2

面试题 16.01. 交换数字
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

示例：

输入: numbers = [1,2]
输出: [2,1]

'''


class Solution(object):
    def swapNumbers(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        # 加减法 a=b-a;b=b-a;a=b+a （要考虑溢出问题）
        # 数组反转 numbers.reverse(); （取巧！！！）
        # es6新特性 [a,b]=[b,a]
        # y = [x, x = y][0]
        # 异或 a=a^b;b=a^b;a=a^b;
        # numbers[:] = numbers[::-1]
        numbers[1] = numbers[1] + numbers[0]
        numbers[0] = numbers[1] - numbers[0]
        numbers[1] = numbers[1] - numbers[0]
        return numbers


        
