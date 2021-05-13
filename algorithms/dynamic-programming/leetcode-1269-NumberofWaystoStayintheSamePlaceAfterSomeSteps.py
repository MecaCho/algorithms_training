# encoding=utf8

'''
1269. Number of Ways to Stay in the Same Place After Some Steps

You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8
 

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6


1269. 停在原地的方案数

有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。

 

示例 1：

输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动
示例  2：

输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动
示例 3：

输入：steps = 4, arrLen = 2
输出：8
 

提示：

1 <= steps <= 500
1 <= arrLen <= 10^6
'''


class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = 1000000007
        max_len = min(steps/2+1, arrLen)
        dp = [[0 for _ in range(max_len+1)] for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1, steps+1):
            for j in range(max_len+1):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
                if j < max_len-1:
                    dp[i][j] += dp[i-1][j+1] 
                dp[i][j] %= MOD

        return dp[-1][0]

# golang solution


'''
func numWays(steps int, arrLen int) int {
	MOD := 1000000007
	maxLen := min(steps/2+1, arrLen)

	dp := make([][]int, steps+1)
	for i := 0; i < steps+1; i++ {
		dp[i] = make([]int, maxLen+1)
	}
	dp[0][0] = 1

	for i := 1; i < steps+1; i++ {
		for j := 0; j < maxLen+1; j++ {
			dp[i][j] = dp[i-1][j]
			if j > 0 {
				dp[i][j] += dp[i-1][j-1]
			}
			if j < maxLen - 1 {
				dp[i][j] += dp[i-1][j+1]
			}
			dp[i][j] %= MOD
		}
	}
    // [[1, 0, 0], [1, 1, 0], [2, 2, 1], [4, 4, 3], [8, 8, 7], [16, 16, 15], [32, 32, 31], [64, 64, 63]]
	// fmt.Println(dp)
	return dp[steps][0]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
'''

# solutions

'''
方法一：动态规划
对于计算方案数的题目，常用的方法是动态规划。对于这道题，需要计算在 \textit{steps}steps 步操作之后，指针位于下标 00 的方案数。

用 \textit{dp}[i][j]dp[i][j] 表示在 ii 步操作之后，指针位于下标 jj 的方案数。其中，ii 的取值范围是 0 \le i \le \textit{steps}0≤i≤steps，jj 的取值范围是 0 \le j \le \textit{arrLen}-10≤j≤arrLen−1。

由于一共执行 \textit{steps}steps 步操作，因此指针所在下标一定不会超过 \textit{steps}steps，可以将 jj 的取值范围进一步缩小到 0 \le j \le \min(\textit{arrLen}-1, \textit{steps})0≤j≤min(arrLen−1,steps)。

当没有进行任何操作时，指针一定位于下标 00，因此动态规划的边界条件是 \textit{dp}[0][0]=1dp[0][0]=1，当 1 \le j \le \min(\textit{arrLen}-1, \textit{steps})1≤j≤min(arrLen−1,steps) 时有 \textit{dp}[0][j]=0dp[0][j]=0。

每一步操作中，指针可以向左或向右移动 11 步，或者停在原地。因此，当 1 \le i \le \textit{steps}1≤i≤steps 时，状态 \textit{dp}[i][j]dp[i][j] 可以从 \textit{dp}[i-1][j-1]dp[i−1][j−1]、\textit{dp}[i-1][j]dp[i−1][j] 和 \textit{dp}[i-1][j+1]dp[i−1][j+1] 这三个状态转移得到。状态转移方程如下：

\textit{dp}[i][j] = \textit{dp}[i-1][j-1]+\textit{dp}[i-1][j]+\textit{dp}[i-1][j+1]
dp[i][j]=dp[i−1][j−1]+dp[i−1][j]+dp[i−1][j+1]

由于指针不能移动到数组范围外，因此对于上述状态转移方程，需要注意下标边界情况。当 j=0j=0 时，\textit{dp}[i-1][j-1]=0dp[i−1][j−1]=0；当 j=\min(\textit{arrLen}-1, \textit{steps})j=min(arrLen−1,steps) 时，\textit{dp}[i-1][j+1]=0dp[i−1][j+1]=0。具体实现时，需要对下标进行判断，避免下标越界。

计算过程中需要对每个状态的值计算模 10^9+710 
9
 +7 后的结果。最终得到 \textit{dp}[\textit{steps}][0]dp[steps][0] 的值即为答案。

JavaC#GolangC++CPython3JavaScript

func numWays(steps, arrLen int) int {
    const mod = 1e9 + 7
    maxColumn := min(arrLen-1, steps)
    dp := make([][]int, steps+1)
    for i := range dp {
        dp[i] = make([]int, maxColumn+1)
    }
    dp[0][0] = 1
    for i := 1; i <= steps; i++ {
        for j := 0; j <= maxColumn; j++ {
            dp[i][j] = dp[i-1][j]
            if j-1 >= 0 {
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod
            }
            if j+1 <= maxColumn {
                dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % mod
            }
        }
    }
    return dp[steps][0]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
上述实现的时间复杂度是 O(\textit{steps} \times \min(\textit{arrLen}, \textit{steps}))O(steps×min(arrLen,steps))，空间复杂度是 O(\textit{steps} \times \min(\textit{arrLen}, \textit{steps}))O(steps×min(arrLen,steps))。

注意到 \textit{dp}dp 的每一行只和上一行有关，因此可以将空间复杂度降低到 O(\min(\textit{arrLen}, \textit{steps}))O(min(arrLen,steps))。

JavaC#GolangC++CPython3JavaScript

func numWays(steps, arrLen int) int {
    const mod = 1e9 + 7
    maxColumn := min(arrLen-1, steps)
    dp := make([]int, maxColumn+1)
    dp[0] = 1
    for i := 1; i <= steps; i++ {
        dpNext := make([]int, maxColumn+1)
        for j := 0; j <= maxColumn; j++ {
            dpNext[j] = dp[j]
            if j-1 >= 0 {
                dpNext[j] = (dpNext[j] + dp[j-1]) % mod
            }
            if j+1 <= maxColumn {
                dpNext[j] = (dpNext[j] + dp[j+1]) % mod
            }
        }
        dp = dpNext
    }
    return dp[0]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(\textit{steps} \times \min(\textit{arrLen}, \textit{steps}))O(steps×min(arrLen,steps))。动态规划需要计算每个状态的值。

空间复杂度：O(\min(\textit{arrLen}, \textit{steps}))O(min(arrLen,steps))。使用空间优化的做法，可以将空间复杂度降低到 O(\min(\textit{arrLen}, \textit{steps}))O(min(arrLen,steps))。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/solution/ting-zai-yuan-di-de-fang-an-shu-by-leetcode-soluti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
