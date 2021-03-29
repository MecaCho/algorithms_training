# encoding=utf8

'''
面试题14- II. 剪绳子 II
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36


提示：

2 <= n <= 1000
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
'''


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
        # print(dp)
        return dp[-1] % 1000000007


class Solution20210329(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1
        MOD = 1000000007
        a, b = n / 3, n % 3
        if b == 0:
            return pow(3, a) % MOD
        if b == 1:
            return pow(3, a-1) * 4 % MOD
        return pow(3, a) * 2 % MOD


class Solution20210329_1(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        def qpow(a, k):
            p = a
            res = 1
            while k > 0:
                if k % 2 == 1:
                    res = res * p % MOD

                p = p * p
                k >>= 1
            return res

        if n < 4:
            return n - 1
        MOD = 1000000007
        a, b = n / 3, n % 3
        if b == 0:
            return pow(3, a) % MOD
        if b == 1:
            return pow(3, a-1) * 4 % MOD
        return pow(3, a) * 2 % MOD
