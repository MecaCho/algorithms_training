
'''

518. 零钱兑换 II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。



示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1


注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数

518. Coin Change 2
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                if i - coin >= 0:
                    dp[i] = dp[i-coin] + dp[i]
        # print(dp)
        return dp[-1]

'''

零钱兑换 II
力扣 (LeetCode)
发布于 4 个月前
6.5k
方法：动态规划
模板：
这是经典的动态编程问题。这是一个可以使用的模板：

定义答案显而易见的基本情况。
制定根据简单的情况计算复杂情况的策略。
将此策略链接到基本情况。
例子：
让我们举一个例子：amount = 11，可用硬币面值有 2 美分，5 美分和 10 美分。 请注意，硬币数量是无限的。

在这里插入图片描述

基本情况：没有硬币或 金币 = 0

如果总金额为 0，那么只有一个组合情况：0。
另一个基本情况是没有硬币，若 amount > 0，则组合情况为 0，若 amount == 0，则组合情况为 1。
在这里插入图片描述

2 美分：

让我们用一种硬币做进一步考虑：2 美分
在这里插入图片描述

很明显，这里可能会有 1 种或 0 种组合。偶数金额为 1 种，奇数金额为 0 种。
首先，所有金额均小于 2 美分不会受到 2 美分硬币的影响。 因此对于 amount = 0 和 amount = 1 的结果没有变化。
从 amount = 2 开始，可以使用 2 美分硬币进行组合。
我们使用 2 美分硬币来组合 amount = 2，则金额 2 美分的组合数等于 amount = 0 的组合数量，即 1。
在这里插入图片描述

同理 amount = 3 的组合数量等于 amount = 1 的组合数量，即 0。
在这里插入图片描述

我们可以推到出 DP 公式为 amount = x: dp[x] = dp[x] + dp[x - coin]，其中 coin = 2 美分，是当前甜腻骄傲硬币的价值。
在这里插入图片描述

2 美分 + 5 美分 + 10 美分：

我们先增加 5 美分的情况，公式是一样的。
在这里插入图片描述

对于 10 美分也是一样的。
在这里插入图片描述

策略为：

从基本情况没有硬币开始，一一添加硬币。
对于每个添加的硬币，我们从金额 0 到 amount 递归的计算组合数量。
算法：

以基本情况没有硬币开始组合数量。dp[0] = 1，然后其余等于 0。
遍历所有硬币面值：
对于每个硬币，我们将从金额 0 遍历到 amount：
对于每个 x，计算组合数：dp[x] += dp[x - coin]。
返回 dp[amount]。
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
复杂度分析

时间复杂度：\mathcal{O}(N \times \textrm{amount})O(N×amount)。其中 N 为 coins 数组的长度。
空间复杂度：\mathcal{O}(\textrm{amount})O(amount)，dp 数组使用的空间。
'''