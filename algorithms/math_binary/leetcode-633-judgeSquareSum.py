'''
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 

示例2:

输入: 3
输出: False


633. Sum of Square Numbers
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
'''

import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        def is_qrt(n):
            sqrt_val = int(math.sqrt(n))
            res = sqrt_val * sqrt_val == n

            return res

        for i in range(int(math.sqrt(c))+1):
            if is_qrt(c-i*i):
                return True
        return False