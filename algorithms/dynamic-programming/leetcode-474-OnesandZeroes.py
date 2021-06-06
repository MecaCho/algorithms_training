# encoding=utf8


'''
474. Ones and Zeroes

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

474. 一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

 

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
 

提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(len(strs)):
            zeros = strs[i].count("0")
            ones = len(strs[i]) - zeros
            for j in range(m, zeros-1, -1):
                for k in range(n, ones-1, -1):
                    dp[j][k] = max(dp[j][k], 1+dp[j-zeros][k-ones])
        return dp[m][n]

      
# solutions


'''
方法一：动态规划
这道题和经典的背包问题非常相似，但是和经典的背包问题只有一种容量不同，这道题有两种容量，即选取的字符串子集中的 00 和 11 的数量上限。

经典的背包问题可以使用二维动态规划求解，两个维度分别是物品和容量。这道题有两种容量，因此需要使用三维动态规划求解，三个维度分别是字符串、00 的容量和 11 的容量。

定义三维数组 \textit{dp}dp，其中 \textit{dp}[i][j][k]dp[i][j][k] 表示在前 ii 个字符串中，使用 jj 个 00 和 kk 个 11 的情况下最多可以得到的字符串数量。假设数组 \textit{str}str 的长度为 ll，则最终答案为 \textit{dp}[l][m][n]dp[l][m][n]。

当没有任何字符串可以使用时，可以得到的字符串数量只能是 00，因此动态规划的边界条件是：当 i=0i=0 时，对任意 0 \le j \le m0≤j≤m 和 0 \le k \le n0≤k≤n，都有 \textit{dp}[i][j][k]=0dp[i][j][k]=0。

当 1 \le i \le l1≤i≤l 时，对于 \textit{strs}strs 中的第 ii 个字符串（计数从 11 开始），首先遍历该字符串得到其中的 00 和 11 的数量，分别记为 \textit{zeros}zeros 和 \textit{ones}ones，然后对于 0 \le j \le m0≤j≤m 和 0 \le k \le n0≤k≤n，计算 \textit{dp}[i][j][k]dp[i][j][k] 的值。

当 00 和 11 的容量分别是 jj 和 kk 时，考虑以下两种情况：

如果 j < \textit{zeros}j<zeros 或 k < \textit{ones}k<ones，则不能选第 ii 个字符串，此时有 \textit{dp}[i][j][k] = \textit{dp}[i - 1][j][k]dp[i][j][k]=dp[i−1][j][k]；

如果 j \ge \textit{zeros}j≥zeros 且 k \ge \textit{ones}k≥ones，则如果不选第 ii 个字符串，有 \textit{dp}[i][j][k] = \textit{dp}[i - 1][j][k]dp[i][j][k]=dp[i−1][j][k]，如果选第 ii 个字符串，有 \textit{dp}[i][j][k] = \textit{dp}[i - 1][j - \textit{zeros}][k - \textit{ones}] + 1dp[i][j][k]=dp[i−1][j−zeros][k−ones]+1，\textit{dp}[i][j][k]dp[i][j][k] 的值应取上面两项中的最大值。

因此状态转移方程如下：

\textit{dp}[i][j][k]=\begin{cases} \textit{dp}[i - 1][j][k], & j<\textit{zeros} ~~ | ~~ k<\textit{ones} \\ \max(\textit{dp}[i - 1][j][k], \textit{dp}[i - 1][j - \textit{zeros}][k - \textit{ones}] + 1), & j \ge \textit{zeros} ~ \& ~ k \ge \textit{ones} \end{cases}
dp[i][j][k]={ 
dp[i−1][j][k],
max(dp[i−1][j][k],dp[i−1][j−zeros][k−ones]+1),
​
  
j<zeros  ∣  k<ones
j≥zeros & k≥ones
​
 

最终得到 \textit{dp}[l][m][n]dp[l][m][n] 的值即为答案。

由此可以得到空间复杂度为 O(lmn)O(lmn) 的实现。

JavaC#JavaScriptGolangC++C

func findMaxForm(strs []string, m, n int) int {
    length := len(strs)
    dp := make([][][]int, length+1)
    for i := range dp {
        dp[i] = make([][]int, m+1)
        for j := range dp[i] {
            dp[i][j] = make([]int, n+1)
        }
    }
    for i, s := range strs {
        zeros := strings.Count(s, "0")
        ones := len(s) - zeros
        for j := 0; j <= m; j++ {
            for k := 0; k <= n; k++ {
                dp[i+1][j][k] = dp[i][j][k]
                if j >= zeros && k >= ones {
                    dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j-zeros][k-ones]+1)
                }
            }
        }
    }
    return dp[length][m][n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
由于 \textit{dp}[i][][]dp[i][][] 的每个元素值的计算只和 \textit{dp}[i-1][][]dp[i−1][][] 的元素值有关，因此可以使用滚动数组的方式，去掉 \textit{dp}dp 的第一个维度，将空间复杂度优化到 O(mn)O(mn)。

实现时，内层循环需采用倒序遍历的方式，这种方式保证转移来的是 \textit{dp}[i-1][][]dp[i−1][][] 中的元素值。

JavaC#JavaScriptGolangC++C

func findMaxForm(strs []string, m, n int) int {
    dp := make([][]int, m+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }
    for _, s := range strs {
        zeros := strings.Count(s, "0")
        ones := len(s) - zeros
        for j := m; j >= zeros; j-- {
            for k := n; k >= ones; k-- {
                dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones]+1)
            }
        }
    }
    return dp[m][n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(lmn + L)O(lmn+L)，其中 ll 是数组 \textit{strs}strs 的长度，mm 和 nn 分别是 00 和 11 的容量，LL 是数组 \textit{strs}strs 中的所有字符串的长度之和。
动态规划需要计算的状态总数是 O(lmn)O(lmn)，每个状态的值需要 O(1)O(1) 的时间计算。
对于数组 \textit{strs}strs 中的每个字符串，都要遍历字符串得到其中的 00 和 11 的数量，因此需要 O(L)O(L) 的时间遍历所有的字符串。
总时间复杂度是 O(lmn + L)O(lmn+L)。

空间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是 00 和 11 的容量。使用空间优化的实现，需要创建 m+1m+1 行 n+1n+1 列的二维数组 \textit{dp}dp。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/ones-and-zeroes/solution/yi-he-ling-by-leetcode-solution-u2z2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
