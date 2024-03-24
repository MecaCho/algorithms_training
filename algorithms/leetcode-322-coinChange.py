# encoding=utf8

'''
322. Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0]
        for i in range(1, amount+1):
            dp.append(float("inf"))
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        return dp[amount] if dp[amount] != float("inf") else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                # print(coin, amount)
                dp[i] = min(dp[i], dp[i-coin] + 1)
        print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1
