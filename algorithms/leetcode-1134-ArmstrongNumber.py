
'''
1134. Armstrong Number
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

 

Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 

Note:

1 <= N <= 10^8

1134. 阿姆斯特朗数
假设存在一个 k 位数 N，其每一位上的数字的 k 次幂的总和也是 N，那么这个数是阿姆斯特朗数。

给你一个正整数 N，让你来判定他是否是阿姆斯特朗数，是则返回 true，不是则返回 false。

 

示例 1：

输入：153
输出：true
示例： 
153 是一个 3 位数，且 153 = 1^3 + 5^3 + 3^3。
示例 2：

输入：123
输出：false
解释： 
123 是一个 3 位数，且 123 != 1^3 + 2^3 + 3^3 = 36。
 

提示：

1 <= N <= 10^8
'''


class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        k = len(str(N))
        tmp = N
        res  = 0
        while N:
            res += (N % 10) ** k
            N = N / 10
        return res == tmp
