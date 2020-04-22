
'''
面试题 08.11. Coin LCCI
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents. (The result may be large, so you should return it modulo 1000000007)

Example1:

 Input: n = 5
 Output: 2
 Explanation: There are two ways:
5=5
5=1+1+1+1+1
Example2:

 Input: n = 10
 Output: 4
 Explanation: There are four ways:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
Notes:

You can assume:

0 <= n <= 1000000

面试题 08.11. 硬币
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000
'''



class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        coins = [25, 10, 5, 1]
        for coin in coins:
            for i in range(1, n+1):
                if i - coin >= 0:

                    dp[i] = (dp[i] + dp[i-coin]) % 1000000007

        # print(dp)
        return dp[-1]