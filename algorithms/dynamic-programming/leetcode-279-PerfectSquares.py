'''
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''



class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        sqrts = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [0]
        for i in range(1, n+1):
            dp.append(i)
            for sqrt_num in sqrts:
                if i - sqrt_num >= 0:
                    dp[i] = min(dp[i], dp[i-sqrt_num] + 1)
        return dp[n]

    
# golang solution

'''
func numSquares(n int) int {
	dp := make([]int, n+1)

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	for i := 1; i <= n; i++ {
		dp[i] = i
		for k := 1; k*k <= i; k++ {
			dp[i] = min(dp[i-k*k]+1, dp[i])
		}
	}
	return dp[n]
}
'''


# solutions

'''
方法一：动态规划
思路及算法

我们可以依据题目的要求写出状态表达式：f[i]f[i] 表示最少需要多少个数的平方来表示整数 ii。

这些数必然落在区间 [1,\sqrt{n}][1, 
n
​
 ]。我们可以枚举这些数，假设当前枚举到 jj，那么我们还需要取若干数的平方，构成 i-j^2i−j 
2
 。此时我们发现该子问题和原问题类似，只是规模变小了。这符合了动态规划的要求，于是我们可以写出状态转移方程。

f[i]=1+\min_{j=1}^{\lfloor\sqrt{i}\rfloor}{f[i-j^2]}
f[i]=1+ 
j=1
min
⌊ 
i
​
 ⌋
​
 f[i−j 
2
 ]

其中 f[0]=0f[0]=0 为边界条件，实际上我们无法表示数字 00，只是为了保证状态转移过程中遇到 jj 恰为 \sqrt{i} 
i
​
  的情况合法。

同时因为计算 f[i]f[i] 时所需要用到的状态仅有 f[i-j^2]f[i−j 
2
 ]，必然小于 ii，因此我们只需要从小到大地枚举 ii 来计算 f[i]f[i] 即可。

代码

C++JavaC#GolangJavaScriptC

func numSquares(n int) int {
    f := make([]int, n+1)
    for i := 1; i <= n; i++ {
        minn := math.MaxInt32
        for j := 1; j*j <= i; j++ {
            minn = min(minn, f[i-j*j])
        }
        f[i] = minn + 1
    }
    return f[n]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n\sqrt{n})O(n 
n
​
 )，其中 nn 为给定的正整数。状态转移方程的时间复杂度为 O(\sqrt{n})O( 
n
​
 )，共需要计算 nn 个状态，因此总时间复杂度为 O(n \sqrt{n})O(n 
n
​
 )。

空间复杂度：O(n)O(n)。我们需要 O(n)O(n) 的空间保存状态。

方法二：数学
思路及算法

一个数学定理可以帮助解决本题：「四平方和定理」。

四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。这给出了本题的答案的上界。

同时四平方和定理包含了一个更强的结论：当且仅当 n \neq 4^k \times (8m+7)n 

​
 =4 
k
 ×(8m+7) 时，nn 可以被表示为至多三个正整数的平方和。因此，当 n = 4^k \times (8m+7)n=4 
k
 ×(8m+7) 时，nn 只能被表示为四个正整数的平方和。此时我们可以直接返回 44。

当 n \neq 4^k \times (8m+7)n 

​
 =4 
k
 ×(8m+7) 时，我们需要判断到底多少个完全平方数能够表示 nn，我们知道答案只会是 1,2,31,2,3 中的一个：

答案为 11 时，则必有 nn 为完全平方数，这很好判断；

答案为 22 时，则有 n=a^2+b^2n=a 
2
 +b 
2
 ，我们只需要枚举所有的 a(1 \leq a \leq \sqrt{n})a(1≤a≤ 
n
​
 )，判断 n-a^2n−a 
2
  是否为完全平方数即可；

答案为 33 时，我们很难在一个优秀的时间复杂度内解决它，但我们只需要检查答案为 11 或 22 的两种情况，即可利用排除法确定答案。

代码

C++JavaC#GolangJavaScriptC

// 判断是否为完全平方数
func isPerfectSquare(x int) bool {
    y := int(math.Sqrt(float64(x)))
    return y*y == x
}

// 判断是否能表示为 4^k*(8m+7)
func checkAnswer4(x int) bool {
    for x%4 == 0 {
        x /= 4
    }
    return x%8 == 7
}

func numSquares(n int) int {
    if isPerfectSquare(n) {
        return 1
    }
    if checkAnswer4(n) {
        return 4
    }
    for i := 1; i*i <= n; i++ {
        j := n - i*i
        if isPerfectSquare(j) {
            return 2
        }
    }
    return 3
}
复杂度分析

时间复杂度：O(\sqrt{n})O( 
n
​
 )，其中 nn 为给定的正整数。最坏情况下答案为 33，我们需要运行所有的判断，而判断答案是否为 11 的时间复杂度为 O(1)O(1)，判断答案是否为 44 的时间复杂度为 O(\log n)O(logn)，剩余判断为 O(\sqrt n)O( 
n
​
 )，因此总时间复杂度为 O(\log n + \sqrt n) = O(\sqrt n)O(logn+ 
n
​
 )=O( 
n
​
 )。

空间复杂度：O(1)O(1)。我们只需要常数的空间保存若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
