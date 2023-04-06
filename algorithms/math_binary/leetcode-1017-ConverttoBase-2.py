# encoding=utf8


'''
leetcode-1017-ConverttoBase-2.py
1017. Convert to Base -2
Given an integer n, return a binary string representing its representation in base -2.

Note that the returned string should not have leading zeros unless the string is "0".

 

Example 1:

Input: n = 2
Output: "110"
Explantion: (-2)2 + (-2)1 = 2
Example 2:

Input: n = 3
Output: "111"
Explantion: (-2)2 + (-2)1 + (-2)0 = 3
Example 3:

Input: n = 4
Output: "100"
Explantion: (-2)2 = 4
 

Constraints:

0 <= n <= 109
'''

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        res = []
        while n:
            remainder = n & 1
            res.append(str(remainder))
            n -= remainder
            n //= -2
        return ''.join(res[::-1])


