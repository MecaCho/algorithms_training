

'''
509. 斐波那契数
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
 

提示：

0 ≤ N ≤ 30

509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.
'''

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        dp = [0,1]
        for i in range(2, N+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[N]

'''
递归
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
func fib(N int) int {
    if N <= 1 {
        return N
    }
    return fib(N-1) + fib(N-2)
}

# 迭代
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N
        if (N == 2):
            return 1

        current = 0
        prev1 = 1
        prev2 = 1

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(3, N+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current


# Contributed by LeetCode user mereck.
class Solution:
  def fib(self, N):
  	golden_ratio = (1 + 5 ** 0.5) / 2
  	return int((golden_ratio ** N + 1) / 5 ** 0.5)

'''
