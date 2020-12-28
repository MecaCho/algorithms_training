# encoding=utf8
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


# solutions

'''
方法一：动态规划
思路与算法

与其余的股票问题类似，我们使用一系列变量存储「买入」的状态，再用一系列变量存储「卖出」的状态，通过动态规划的方法即可解决本题。

我们用 \textit{buy}[i][j]buy[i][j] 表示对于数组 \textit{prices}[0..i]prices[0..i] 中的价格而言，进行恰好 jj 笔交易，并且当前手上持有一支股票，这种情况下的最大利润；用 \textit{sell}[i][j]sell[i][j] 表示恰好进行 jj 笔交易，并且当前手上不持有股票，这种情况下的最大利润。

那么我们可以对状态转移方程进行推导。对于 \textit{buy}[i][j]buy[i][j]，我们考虑当前手上持有的股票是否是在第 ii 天买入的。如果是第 ii 天买入的，那么在第 i-1i−1 天时，我们手上不持有股票，对应状态 \textit{sell}[i-1][j]sell[i−1][j]，并且需要扣除 \textit{prices}[i]prices[i] 的买入花费；如果不是第 ii 天买入的，那么在第 i-1i−1 天时，我们手上持有股票，对应状态 \textit{buy}[i][j]buy[i][j]。那么我们可以得到状态转移方程：

\textit{buy}[i][j] = \max \big\{ \textit{buy}[i-1][j], \textit{sell}[i-1][j] - \textit{price}[i] \big\}
buy[i][j]=max{buy[i−1][j],sell[i−1][j]−price[i]}

同理对于 \textit{sell}[i][j]sell[i][j]，如果是第 ii 天卖出的，那么在第 i-1i−1 天时，我们手上持有股票，对应状态 \textit{buy}[i-1][j-1]buy[i−1][j−1]，并且需要增加 \textit{prices}[i]prices[i] 的卖出收益；如果不是第 ii 天卖出的，那么在第 i-1i−1 天时，我们手上不持有股票，对应状态 \textit{sell}[i-1][j]sell[i−1][j]。那么我们可以得到状态转移方程：

\textit{sell}[i][j] = \max \big\{ \textit{sell}[i-1][j], \textit{buy}[i-1][j-1] + \textit{price}[i] \big\}
sell[i][j]=max{sell[i−1][j],buy[i−1][j−1]+price[i]}

由于在所有的 nn 天结束后，手上不持有股票对应的最大利润一定是严格由于手上持有股票对应的最大利润的，然而完成的交易数并不是越多越好（例如数组 \textit{prices}prices 单调递减，我们不进行任何交易才是最优的），因此最终的答案即为 \textit{sell}[n-1][0..k]sell[n−1][0..k] 中的最大值。

细节

在上述的状态转移方程中，确定边界条件是非常重要的步骤。我们可以考虑将所有的 \textit{buy}[0][0..k]buy[0][0..k] 以及 \textit{sell}[0][0..k]sell[0][0..k] 设置为边界。

对于 \textit{buy}[0][0..k]buy[0][0..k]，由于只有 \textit{prices}[0]prices[0] 唯一的股价，因此我们不可能进行过任何交易，那么我们可以将所有的 \textit{buy}[0][1..k]buy[0][1..k] 设置为一个非常小的值，表示不合法的状态。而对于 \textit{buy}[0][0]buy[0][0]，它的值为 -\textit{prices}[0]−prices[0]，即「我们在第 00 天以 \textit{prices}[0]prices[0] 的价格买入股票」是唯一满足手上持有股票的方法。

对于 \textit{sell}[0][0..k]sell[0][0..k]，同理我们可以将所有的 \textit{sell}[0][1..k]sell[0][1..k] 设置为一个非常小的值，表示不合法的状态。而对于 \textit{sell}[0][0]sell[0][0]，它的值为 00，即「我们在第 00 天不做任何事」是唯一满足手上不持有股票的方法。

在设置完边界之后，我们就可以使用二重循环，在 i\in [1,n), j \in [0, k]i∈[1,n),j∈[0,k] 的范围内进行状态转移。需要注意的是，\textit{sell}[i][j]sell[i][j] 的状态转移方程中包含 \textit{buy}[i-1][j-1]buy[i−1][j−1]，在 j=0j=0 时其表示不合法的状态，因此在 j=0j=0 时，我们无需对 \textit{sell}[i][j]sell[i][j] 进行转移，让其保持值为 00 即可。

最后需要注意的是，本题中 kk 的最大值可以达到 10^910 
9
 ，然而这是毫无意义的，因为 nn 天最多只能进行 \lfloor \frac{n}{2} \rfloor⌊ 
2
n
​	
 ⌋ 笔交易，其中 \lfloor x \rfloor⌊x⌋ 表示对 xx 向下取整。因此我们可以将 kk 对 \lfloor \frac{n}{2} \rfloor⌊ 
2
n
​	
 ⌋ 取较小值之后再进行动态规划。

代码

C++JavaPython3GolangCJavaScript

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);  

        return max(sell[n - 1])
注意到在状态转移方程中，\textit{buy}[i][j]buy[i][j] 和 \textit{sell}[i][j]sell[i][j] 都从 \textit{buy}[i-1][..]buy[i−1][..] 以及 \textit{sell}[i-1][..]sell[i−1][..] 转移而来，因此我们可以使用一维数组而不是二维数组进行状态转移，即：

\begin{cases} b[j] \leftarrow \max \big\{ b[j], s[j] - \textit{price}[i] \big\} \\ \\ s[j] \leftarrow \max \big\{ s[j], b[j-1] + \textit{price}[i] \big\} \end{cases}
⎩
⎪
⎪
⎨
⎪
⎪
⎧
​	
  
b[j]←max{b[j],s[j]−price[i]}
s[j]←max{s[j],b[j−1]+price[i]}
​	
 

这样的状态转移方程会因为状态的覆盖而变得不同。例如如果我们先计算 \textit{b}b 而后计算 ss，那么在计算到 s[j]s[j] 时，其状态转移方程中包含的 b[j-1]b[j−1] 这一项的值已经被覆盖了，即本来应当是从二维表示中的 \textit{buy}[i-1][j-1]buy[i−1][j−1] 转移而来，而现在却变成了 \textit{buy}[i][j-1]buy[i][j−1]。

但其仍然是正确的。我们考虑 \textit{buy}[i][j-1]buy[i][j−1] 的状态转移方程：

b[j-1] \leftarrow \textit{buy}[i][j-1] = \max \big\{ \textit{buy}[i-1][j-1], \textit{sell}[i-1][j-1] - \textit{price}[i] \big\}
b[j−1]←buy[i][j−1]=max{buy[i−1][j−1],sell[i−1][j−1]−price[i]}

那么 s[j]s[j] 的状态转移方程实际上为：

s[j] \leftarrow \max \big\{ s[j], \textit{buy}[i-1][j-1] + \textit{prices}[i], \textit{sell}[i-1][j-1] \big\}
s[j]←max{s[j],buy[i−1][j−1]+prices[i],sell[i−1][j−1]}

根据 \textit{buy}[i-1][j-1]buy[i−1][j−1] 的状态转移方程，\textit{buy}[i-1][j-1] \geq \textit{sell}[i-1][j-1] - \textit{prices}[i]buy[i−1][j−1]≥sell[i−1][j−1]−prices[i]，因此有：

\textit{buy}[i-1][j-1] + \textit{prices}[i] \geq \textit{sell}[i-1][j-1]
buy[i−1][j−1]+prices[i]≥sell[i−1][j−1]

那么 \textit{sell}[i-1][j-1]sell[i−1][j−1] 这一项在 s[j]s[j] 的状态转移方程中不起任何作用，因此即使 b[j-1]b[j−1] 被覆盖了，状态转移方程本质上仍然是正确的。

C++JavaPython3GolangJavaScriptC

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [0] * (k + 1)
        sell = [0] * (k + 1)

        buy[0], sell[0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[i] = sell[i] = float("-inf")

        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i]); 

        return max(sell)
复杂度分析

时间复杂度：O(n\min(n, k))O(nmin(n,k))，其中 nn 是数组 \textit{prices}prices 的大小，即我们使用二重循环进行动态规划需要的时间。

空间复杂度：O(n\min(n, k))O(nmin(n,k)) 或 O(\min(n, k))O(min(n,k))，取决于我们使用二维数组还是一维数组进行动态规划。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-iv-by-8xtkp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''