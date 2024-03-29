# encoding=utf8

'''
400. 第N个数字
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32位整数范围内 ( n < 231)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。

400. Nth Digit
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''




class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [10]
        j = 2
        step = 10
        while step <= 2**31 and n >= step:
            step += j*9*(pow(10, (j-1)))
            steps.append(step)
            j += 1
        if n < 10:
            return n
        for k in range(1, len(steps)+1):
            if n < steps[k]:
                return int(str(10**k + (n - steps[k-1]) / (k+1))[(n-steps[k-1])%(k+1)])


# Check the same-length ranges 1-9, 10-99, 100-999, 1000-9999, etc.

# Python:

def findNthDigit(self, n):
    n -= 1
    for digits in range(1, 11):
        first = 10**(digits - 1)
        if n < 9 * first * digits:
            return int(str(first + n/digits)[n%digits])
        n -= 9 * first * digits
