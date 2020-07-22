'''
188. Best Time to Buy and Sell Stock IV
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


188. 买卖股票的最佳时机 IV
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
'''


class Solution(object):

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k > len(prices) / 2:
            return sum(
                    [prices[i + 1] - prices[i] if (prices[i + 1] > prices[i]) else 0 for i in xrange(len(prices) - 1)])

        asset, cash = [0] * (k + 1), [float("-inf")] * (1 + k)
        for price in prices:
            for i in xrange(1, k + 1):
                asset[i] = max(asset[i], cash[i] + price)
                cash[i] = max(cash[i], asset[i - 1] - price)
        return asset[-1]



class SolutionTemplate(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
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