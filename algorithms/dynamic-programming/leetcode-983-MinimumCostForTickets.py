# encoding=utf8

'''
983. 最低票价
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。



示例 1：

输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。
示例 2：

输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
输出：17
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。
你总共花了 $17，并完成了你计划的每一天旅行。


提示：

1 <= days.length <= 365
1 <= days[i] <= 365
days 按顺序严格递增
costs.length == 3
1 <= costs[i] <= 1000

983. Minimum Cost For Tickets
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.



Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.


Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
'''




class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0]
        d_days = [1,7,30]
        max_day = max(days) + 1
        for i in range(1, max_day):
            dp.append(dp[-1]+min(costs))
            if i in days:
                for j in range(len(costs)):
                    if i - d_days[j] >= 0:
                        # print(i, j, costs[j])
                        dp[i] = min(dp[i-d_days[j]] + costs[j], dp[i])
                    else:
                        dp[i] = min(costs[j], dp[i])
            else:
                dp[i] = dp[i-1]
        # print(dp)
        return dp[days[-1]]


'''
方法一：记忆化搜索（日期变量型）
思路和算法

我们用 \textit{dp}(i)dp(i) 来表示从第 ii 天开始到一年的结束，我们需要花的钱。考虑到一张通行证可以让我们在「接下来」的若干天进行旅行，所以我们「从后往前」倒着进行动态规划。

对于一年中的任意一天：

如果这一天不是必须出行的日期，那我们可以贪心地选择不买。这是因为如果今天不用出行，那么也不必购买通行证，并且通行证越晚买越好。所以有 \textit{dp}(i) = \textit{dp}(i + 1)dp(i)=dp(i+1)；

如果这一天是必须出行的日期，我们可以选择买 11，77 或 3030 天的通行证。若我们购买了 jj 天的通行证，那么接下来的 j - 1j−1 天，我们都不再需要购买通行证，只需要考虑第 i + ji+j 天及以后即可。因此，我们有

\textit{dp}(i) = \textit{cost}(j) + \max\{\textit{dp}(i + j)\}, \quad j \in \{1, 7, 30\}
dp(i)=cost(j)+max{dp(i+j)},j∈{1,7,30}

其中 \textit{cost}(j)cost(j) 表示 jj 天通行证的价格。为什么我们只需要考虑第 i+ji+j 天及以后呢？这里和第一条的贪心思路是一样的，如果我们需要购买通行证，那么一定越晚买越好，在握着一张有效的通行证的时候购买其它的通行证显然是不划算的。

由于我们是倒着进行动态规划的，因此我们可以使用记忆化搜索，减少代码的编写难度。我们使用一个长度为 366366 的数组（因为天数是 [1, 365][1,365]，而数组的下标是从 00 开始的）存储所有的动态规划结果，这样所有的 \textit{dp}(i)dp(i) 只会被计算一次（和普通的动态规划相同），时间复杂度不会增大。

最终的答案记为 \textit{dp}(1)dp(1)。

JavaPython3C++Golang
class Solution {
    int[] costs;
    Integer[] memo;
    Set<Integer> dayset;

    public int mincostTickets(int[] days, int[] costs) {
        this.costs = costs;
        memo = new Integer[366];
        dayset = new HashSet();
        for (int d: days) {
            dayset.add(d);
        }
        return dp(1);
    }

    public int dp(int i) {
        if (i > 365) {
            return 0;
        }
        if (memo[i] != null) {
            return memo[i];
        }
        if (dayset.contains(i)) {
            memo[i] = Math.min(Math.min(dp(i + 1) + costs[0], dp(i + 7) + costs[1]), dp(i + 30) + costs[2]);
        }
        else {
            memo[i] = dp(i + 1);
        }
        return memo[i];
    }
}
复杂度分析

时间复杂度：O(W)O(W)，其中 W = 365W=365 是旅行计划中日期的最大值，我们需要计算 WW 个解，而每个解最多需要查询 33 个其他的解，因此计算量为 O(3 * W)=O(W)O(3∗W)=O(W)。

空间复杂度：O(W)O(W)，我们需要长度为 O(W)O(W) 的数组来存储所有的解。

方法二：记忆化搜索（窗口变量型）
思路

方法一需要遍历一年中所有的天数，无论 \textit{days}days 的长度是多少。

但是观察方法一的递推式，我们可以看到，如果我们查询 \textit{dp}(i)dp(i)，而第 ii 天我们又不需要出行的话，那么 \textit{dp}dp 函数会一直向后计算 \textit{dp}(i + 1) = \textit{dp}(i + 2) = \textit{dp}(i + 3)dp(i+1)=dp(i+2)=dp(i+3) 一直到一年结束或者有一天我们需要出行为止。那么我们其实可以直接跳过这些不需要出行的日期，直接找到下一个需要出行的日期。

算法

现在，我们令 \textit{dp}(i)dp(i) 表示能够完成从第 \textit{days}[i]days[i] 天到最后的旅行计划的最小花费（注意，不再是第 ii 天到最后的最小花费）。令 j_1j 
1
​	
  是满足 \textit{days}[j_1] >= \textit{days}[i] + 1days[j 
1
​	
 ]>=days[i]+1 的最小下标，j_7j 
7
​	
  是满足 \textit{days}[j_7] >= \textit{days}[i] + 7days[j 
7
​	
 ]>=days[i]+7 的最小下标， j_{30}j 
30
​	
  是满足 \textit{days}[j_{30}] >= \textit{days}[i] + 30days[j 
30
​	
 ]>=days[i]+30 的最小下标，那么就有：

\textit{dp}(i) = \min(\textit{dp}(j_1) + \textit{costs}[0], \textit{dp}(j_7) + \textit{costs}[1], \textit{dp}(j_{30}) + \textit{costs}[2])
dp(i)=min(dp(j 
1
​	
 )+costs[0],dp(j 
7
​	
 )+costs[1],dp(j 
30
​	
 )+costs[2])

JavaPython3C++Golang
class Solution {
    int[] days, costs;
    Integer[] memo;
    int[] durations = new int[]{1, 7, 30};

    public int mincostTickets(int[] days, int[] costs) {
        this.days = days;
        this.costs = costs;
        memo = new Integer[days.length];
        return dp(0);
    }

    public int dp(int i) {
        if (i >= days.length) {
            return 0;
        }
        if (memo[i] != null) {
            return memo[i];
        }
        memo[i] = Integer.MAX_VALUE;
        int j = i;
        for (int k = 0; k < 3; ++k) {
            while (j < days.length && days[j] < days[i] + durations[k]) {
                j++;
            }
            memo[i] = Math.min(memo[i], dp(j) + costs[k]);
        }
        return memo[i];
    }
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是出行日期的数量，我们需要计算 NN 个解，而计算每个解的过程中最多将指针挪动 3030 步，计算量为 O(30 * N)=O(N)O(30∗N)=O(N)。

空间复杂度：O(N)O(N)，我们需要长度为 O(N)O(N) 的数组来存储所有的解。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets/solution/zui-di-piao-jie-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
