# encoding=utf8

'''
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

'''
动态规划
'''
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 1
        cash, asset = [float('-inf')] * (k + 1), [0] * (k + 1)
        for price in prices:
            for i in range(1, k + 1):
                cash[i] = max(cash[i], asset[i - 1] - price)
                asset[i] = max(asset[i], cash[i] + price)
        return asset[-1]


def init():
    print("hello")
      
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def max_profit(arr):
            min_price = arr[0] if arr else 0
            profit = 0
            for i in arr:
                min_price = min(i, min_price)
                profit = max(i-min_price, profit)
            return profit

        return max_profit(prices)

    @staticmethod
    def max_profit():
        print("staticmethod")

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            prices[i] = prices[i] - min_price
        return max(prices)
      
'''
作者：qiuwenqi
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/python-jian-dan-suan-fa-ji-bai-liao-10000-de-yong-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

if __name__ == '__main__':
    demo = Solution()
    demo.maxProfit([1,2,4,5,9])
    demo.max_profit()

