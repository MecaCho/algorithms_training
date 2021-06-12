# encoding=utf8

'''
5399. 数位成本和为目标值的最大数字
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。



示例 1：

输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "997" 也是满足要求的数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
示例 2：

输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
示例 3：

输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。
示例 4：

输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"


提示：

cost.length == 9
1 <= cost[i] <= 5000
1 <= target <= 5000

5399. Form Largest Integer With Digits That Add up to Target
Given an array of integers cost and an integer target. Return the maximum integer you can paint under the following rules:

The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
The total cost used must be equal to target.
Integer does not have digits 0.
Since the answer may be too large, return it as string.

If there is no way to paint any integer given the condition, return "0".



Example 1:

Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: "7772"
Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "997", but "7772" is the largest number.
Digit    cost
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
Example 2:

Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
Output: "85"
Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
Example 3:

Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
Output: "0"
Explanation: It's not possible to paint any integer with total cost equal to target.
Example 4:

Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
Output: "32211"


Constraints:

cost.length == 9
1 <= cost[i] <= 5000
1 <= target <= 5000
'''


class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [-float("inf") for _ in range(target + 1)]

        nums = [[] for _ in range(target + 1)]

        costs = []
        for i in range(len(cost)):
            costs.append((cost[i], -i - 1))

        costs = sorted(costs)
        hash_map = {}
        for k, v in costs:
            if k not in hash_map:
                hash_map[k] = str(-v)

        for i in range(len(cost)):
            if cost[i] <= target:
                dp[cost[i]] = 1
                nums[cost[i]] = [cost[i]]
                for j in range(target + 1):
                    if j - cost[i] >= 0:
                        if dp[j - cost[i]] + 1 >= dp[j]:
                            nums[j] = nums[j - cost[i]] + [cost[i]]
                        dp[j] = max(dp[j - cost[i]] + 1, dp[j])

        if dp[target] == -float("inf"):
            return "0"

        res = ""

        for num in nums[-1][::-1]:
            res += hash_map[num]
        return res


'''
Use dynamic programming to find the maximum digits to paint given a total cost.
Build the largest number possible using this DP table.
'''

class Solution1(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """

        dp = [float("-inf")] * (target + 1)
        dp[0] = 0

        for c in cost:
            for j in range(c, target + 1):
                dp[j] = max(dp[j], dp[j - c] + 1)
        
        if dp[target] < 0:
            return "0"
        
        ans = list()
        j = target
        for i in range(8, -1, -1):
            c = cost[i]
            while j >= c and dp[j] == dp[j - c] + 1:
                ans.append(str(i + 1))
                j -= c

        return "".join(ans)

# solutions

‘’‘
方法一：动态规划
若两个整数位数不同，位数更多的整数必然大于位数小的整数。因此我们需要先计算出可以得到的整数的最大位数。

该问题可以看作是恰好装满背包容量为 \textit{target}target，物品重量为 \textit{cost}[i]cost[i]，价值为 11 的完全背包问题。

对于该问题，定义二维数组 \textit{dp}dp，其中 \textit{dp}[i+1][j]dp[i+1][j] 表示使用前 ii 个数位且花费总成本恰好为 jj 时的最大位数，若花费总成本无法为 jj，则规定其为 -\infty−∞。特别地，\textit{dp}[0][]dp[0][] 为不选任何数位的状态，因此除了 \textit{dp}[0][0]dp[0][0] 为 00，其余 \textit{dp}[0][j]dp[0][j] 全为 -\infty−∞。

对于第 ii 个数位，考虑花费总成本恰好为 jj 时的状态转移：

若 j<\textit{cost}[i]j<cost[i]，则无法选第 ii 个数位，此时有 \textit{dp}[i+1][j]=\textit{dp}[i][j]dp[i+1][j]=dp[i][j]；
若 j\ge \textit{cost}[i]j≥cost[i]，存在选或不选两种决策，不选时有 \textit{dp}[i+1][j]=\textit{dp}[i][j]dp[i+1][j]=dp[i][j]，选时由于第 ii 个数位可以重复选择，可以从使用前 ii 个数位且花费总成本恰好为 j-\textit{cost}[i]j−cost[i] 的状态转移过来，即 \textit{dp}[i+1][j]=\textit{dp}[i+1][j-\textit{cost}[i]]+1dp[i+1][j]=dp[i+1][j−cost[i]]+1。取这两种决策的最大值。
因此状态转移方程为：

\textit{dp}[i+1][j]= \begin{cases} \textit{dp}[i][j],& j<\textit{cost}[i] \\ \max(\textit{dp}[i][j],\textit{dp}[i+1][j-\textit{cost}[i]]+1), & j\ge \textit{cost}[i] \end{cases}
dp[i+1][j]={ 
dp[i][j],
max(dp[i][j],dp[i+1][j−cost[i]]+1),
​
  
j<cost[i]
j≥cost[i]
​
 

\textit{dp}[9][target]dp[9][target] 即为可以得到的整数的最大位数，若其小于 00 则说明我们无法得到满足要求的整数，返回 \texttt{"0"}"0"。否则，我们需要生成一个整数，其位数为 \textit{dp}[9][target]dp[9][target] 且数值最大。

为了生成该整数，我们可以用一个额外的二维数组 \textit{from}from，在状态转移时记录转移来源。这样我们可以从最终状态 \textit{dp}[9][target]dp[9][target] 顺着 \textit{from}from 不断倒退，直至达到起始状态 \textit{dp}[0][0]dp[0][0]。在倒退状态时，若转移来源是 \textit{dp}[i+1][j-\textit{cost}[i]]dp[i+1][j−cost[i]] 则说明我们选取了第 ii 个数位。

根据转移方程：

若 j<\textit{cost}[i]j<cost[i]，有 \textit{from}[i+1][j]=jfrom[i+1][j]=j；
若 j\ge \textit{cost}[i]j≥cost[i]，当 \textit{dp}[i][j]>\textit{dp}[i+1][j-\textit{cost}[i]]+1dp[i][j]>dp[i+1][j−cost[i]]+1 时有 \textit{from}[i+1][j]=jfrom[i+1][j]=j，否则有 \textit{from}[i+1][j]=j-\textit{cost}[i]from[i+1][j]=j−cost[i]。
注意我们并没有记录转移来源是 ii 还是 i+1i+1，这是因为若 \textit{from}[i+1][j]from[i+1][j] 的值为 jj，则必定从 ii 转移过来，否则必定从 i+1i+1 转移过来。

此外，由于我们是从最大的数位向最小的数位倒退，为使生成的整数尽可能地大，对于当前数位应尽可能多地选取，所以当 \textit{dp}[i][j]dp[i][j] 与 \textit{dp}[i+1][j-\textit{cost}[i]]+1dp[i+1][j−cost[i]]+1 相等时，我们选择从后者转移过来。

这样我们就得到了每个数位的选择次数，为使生成的整数尽可能地大，我们应按照从大到小的顺序填入各个数位。由于该顺序与倒退状态的顺序一致，我们可以在倒退状态时，将当前数位直接加入生成的整数末尾。

代码实现时，-\infty−∞ 可以用一个非常小的负数表示，保证转移时对于值为 -\infty−∞ 的状态，其 +1+1 之后仍然为负数。

C++JavaC#GolangJavaScriptCPython3

func largestNumber(cost []int, target int) string {
    dp := make([][]int, 10)
    from := make([][]int, 10)
    for i := range dp {
        dp[i] = make([]int, target+1)
        for j := range dp[i] {
            dp[i][j] = math.MinInt32
        }
        from[i] = make([]int, target+1)
    }
    dp[0][0] = 0
    for i, c := range cost {
        for j := 0; j <= target; j++ {
            if j < c {
                dp[i+1][j] = dp[i][j]
                from[i+1][j] = j
            } else {
                if dp[i][j] > dp[i+1][j-c]+1 {
                    dp[i+1][j] = dp[i][j]
                    from[i+1][j] = j
                } else {
                    dp[i+1][j] = dp[i+1][j-c] + 1
                    from[i+1][j] = j - c
                }
            }
        }
    }
    if dp[9][target] < 0 {
        return "0"
    }
    ans := make([]byte, 0, dp[9][target])
    i, j := 9, target
    for i > 0 {
        if j == from[i][j] {
            i--
        } else {
            ans = append(ans, '0'+byte(i))
            j = from[i][j]
        }
    }
    return string(ans)
}
上述代码有两处空间优化：

其一是滚动数组优化。由于 \textit{dp}[i+1][]dp[i+1][] 每个元素值的计算只与 \textit{dp}[i+1][]dp[i+1][] 和 \textit{dp}[i][]dp[i][] 的元素值有关，因此可以使用滚动数组的方式，去掉 \textit{dp}dp 的第一个维度。

其二是去掉 \textit{from}from 数组。在状态倒退时，直接根据 \textit{dp}[j]dp[j] 与 \textit{dp}[j-\textit{cost}[i]]+1dp[j−cost[i]]+1 是否相等来判断，若二者相等则说明是从 \textit{dp}[j-\textit{cost}[i]]dp[j−cost[i]] 转移而来，即选择了第 ii 个数位。

C++JavaC#GolangJavaScriptCPython3

func largestNumber(cost []int, target int) string {
    dp := make([]int, target+1)
    for i := range dp {
        dp[i] = math.MinInt32
    }
    dp[0] = 0
    for _, c := range cost {
        for j := c; j <= target; j++ {
            dp[j] = max(dp[j], dp[j-c]+1)
        }
    }
    if dp[target] < 0 {
        return "0"
    }
    ans := make([]byte, 0, dp[target])
    for i, j := 8, target; i >= 0; i-- {
        for c := cost[i]; j >= c && dp[j] == dp[j-c]+1; j -= c {
            ans = append(ans, byte('1'+i))
        }
    }
    return string(ans)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n\cdot\textit{target})O(n⋅target)。其中 nn 是数组 \textit{cost}cost 的长度。

空间复杂度：O(\textit{target})O(target)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target/solution/shu-wei-cheng-ben-he-wei-mu-biao-zhi-de-dnh86/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
’‘’


