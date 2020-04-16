

'''
264. 丑数 II
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。

264. Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.


'''


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i2 ,i3 ,i5 = 0 ,0 ,0
        for i in range(1691):

            num = min(res[i2 ] *2, res[i3 ] *3, res[i5 ] *5)

            if len(res) == n:
                break

            if num == res[i2 ] *2:
                i2 += 1
            if num == res[i3 ] *3:
                i3 += 1
            if num == res[i5 ] *5:
                i5 += 1
            # print(num, i2, i3, i5,res)
            res.append(num)
        # print(res)
        return res[-1]
