# encoding=utf8

'''
123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

123. 买卖股票的最佳时机 III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        dp_1, dp_2 = [[0, 0]]*len(prices), [[0, 0]]*len(prices)

        dp_1[-1][0] = 0
        dp_1[-1][1] = -99999

        dp_2[-1][0] = 0
        dp_2[-1][1] = -99999

        for i in range(len(prices)):
            dp_1[i][0] = max(dp_1[i-1][0], dp_1[i-1][1] + prices[i])
            dp_1[i][1] = max(dp_1[i-1][1], -prices[i])

            dp_2[i][0] = max(dp_2[i-1][0], dp_2[i-1][1] + prices[i])
            dp_2[i][1] = max(dp_2[i-1][1], dp_1[i-1][0] - prices[i])

        return max([dp_2[i][0], dp_1[i][0], 0])

class SolutionTemplate(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 2
        dp = []
        if k > len(prices) / 2:
            return sum([prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1]])
        for j, price in enumerate(prices):
            dp.append([[0], [-float("inf")]])
            for i in range(1, k+1):
                dp[j][0].append(-float("inf"))
                dp[j][1].append(-float("inf"))
                if i == 1:
                    dp[j][1][1] = -price
                if j > 0:
                    dp[j][0][i] = max(dp[j-1][0][i], dp[j-1][1][i]+price)
                    dp[j][1][i] = max(dp[j-1][0][i-1]-price, dp[j-1][1][i])
        # print(dp)
        return max(dp[-1][0]) if dp else 0



class Solution20210109(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 2
        dp = []
        if k > len(prices) / 2:
            return sum([prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1]])
        for j, price in enumerate(prices):
            dp.append([[0], [-float("inf")]])
            for i in range(1, k+1):
                dp[j][0].append(-float("inf"))
                dp[j][1].append(-float("inf"))
                if i == 1:
                    dp[j][1][1] = -price
                if j > 0:
                    dp[j][0][i] = max(dp[j-1][0][i], dp[j-1][1][i]+price)
                    dp[j][1][i] = max(dp[j-1][0][i-1]-price, dp[j-1][1][i])
        # print(dp)
        return max(dp[-1][0]) if dp else 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp0 = [0, -prices[0]]
        dp1 = [0, -prices[0]]
        for i in range(1, n):
            dp0[0] = max(dp0[1]+prices[i], dp0[0])
            dp0[1] = max(dp0[1], -prices[i])
            dp1[0] = max(dp1[1]+prices[i], dp1[0])
            dp1[1] = max(dp0[0]-prices[i], dp1[1])
        return dp1[0]
